# -*- coding: utf-8 -*-
import scrapy
from JDDetail.items import JDDetailItem
from scrapy_redis.spiders import RedisSpider
from scrapy.utils.project import get_project_settings
import re,json


class JDDetailSpide(RedisSpider):
    # 获取指定商品的商品详情
    name = 'JDDetailSpide'
    allowed_domains = ['www.jd.com']
    redis_key = 'JDDetailSpider:start_urls'

    settings = get_project_settings()
    comment_url = settings['COMMENT_EXCERPT_URL']
    price_url = settings['PRICE_URL']

    def parse(self, response):
        item = JDDetailItem()

        # 全球购
        if 'hk' in response.url:
            global_buy = True
        else:
            global_buy = False

        # 商品名
        raw_name = re.findall(r'<div class="sku-name">(.*?)</div>', response.text, re.S)[0].strip()
        if '京东精选' in raw_name:
            jd_sel = True
        else:
            jd_sel = False

        # 确保商品名无多余字符，如可能出现的 "京东精选"
        name_list = raw_name.split('>')
        name = name_list[len(name_list) - 1].strip()

        # 全球购商铺名提取方法不同
        if not global_buy:
            owner_list = response.xpath('//div[@class="J-hove-wrap EDropdown fr"]/div[@class="item"]/div[@class="name"]'
                                        '/a/text()').extract()
        else:
            owner_list = response.xpath('//div[@class="shopName"]/strong/span/a/text()').extract()

        # 是否自营
        if len(owner_list) == 0:
            owner = '自营'
            flag = True
        else:
            owner = owner_list[0]
            if '自营' in owner:
                flag = True
            else:
                flag = False
        num = re.findall(r'(\d+)', response.url)[0]

        item['name'] = name
        item['owner'] = owner
        item['flag'] = flag
        item['global_buy'] = global_buy
        item['jd_sel'] = jd_sel
        item['num'] = num
        print("11111")
        print(item)
        # 请求价格json数据
        yield scrapy.Request(self.price_url.format(num), meta={'item': item}, callback=self.get_price,dont_filter=True)

    def get_price(self, response):
        item = response.meta['item']
        print("-----")
        print(item)
        price_json = json.loads(response.text)
        item['price'] = price_json[0]['p']
        num = item['num']

        # 请求评论总结json数据
        yield scrapy.Request(self.comment_url.format(num), meta={'item': item}, callback=self.get_comment,dont_filter=True)

    def get_comment(self, response):
        item = response.meta['item']

        comment_json = json.loads(response.text)
        comment_json = comment_json['CommentsCount'][0]

        item['comment_count'] = comment_json['CommentCount']
        item['good_count'] = comment_json['GoodCount']
        item['default_good_count'] = comment_json['DefaultGoodCount']
        item['general_count'] = comment_json['GeneralCount']
        item['poor_count'] = comment_json['PoorCount']
        item['after_count'] = comment_json['AfterCount']
        item['good_rate'] = comment_json['GoodRate']
        item['general_rate'] = comment_json['GeneralRate']
        item['poor_rate'] = comment_json['PoorRate']
        item['average_score'] = comment_json['AverageScore']

        yield item


