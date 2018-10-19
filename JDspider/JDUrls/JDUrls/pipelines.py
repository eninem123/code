# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import redis
import json

# class JDUrlsPipeline(object):
#     def __init__(self):
#         self.settings = get_project_settings()
#         self.detail_url = self.settings['GOODS_DETAIL_URL']
#         self.comment_url = self.settings['COMMENT_URL']
#
#         self.f = open("urls.json", "w")
#
#     def process_item(self, item, spider):
#         # 将商品编号整合成detail-relate url 和comment-relate url后存到服务器redis数据库
#         for n in item['num_list']:
#             item['num_list'] = n
#             item['detail_url'] = self.detail_url.format(n)
#             item['comment_url'] = self.comment_url.format(n)
#             content = json.dumps(dict(item)) + ",\n"
#             self.f.write(content)
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()


class JDUrlsPipeline(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.detail_url = self.settings['GOODS_DETAIL_URL']
        self.comment_url = self.settings['COMMENT_URL']

        self.r = redis.Redis(host=self.settings['REDIS_HOST'], port=self.settings['REDIS_PORT'],
                             )

    def process_item(self, item, spider):
        # 将商品编号整合成detail-relate url 和comment-relate url后存到服务器redis数据库
        for n in item['num_list']:
            self.r.lpush('JDDetailSpider:start_urls', self.detail_url.format(n))
            self.r.lpush('JDCommentSpider:start_urls', self.comment_url.format(n))

