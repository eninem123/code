# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品名称TINYTEXT
    name = scrapy.Field()
    # 商品价格FLOAT
    price = scrapy.Field()
    # 商铺名TINYTEXT
    owner = scrapy.Field()
    # 京东精选TINYINT
    jd_sel = scrapy.Field()
    # 全球购TINYINT
    global_buy = scrapy.Field()
    # 自营标志TINYINT
    flag = scrapy.Field()
    # 评论总数INT
    comment_count = scrapy.Field()
    # 好评数INT
    good_count = scrapy.Field()
    # 默认好评数INT
    default_good_count = scrapy.Field()
    # INT
    general_count = scrapy.Field()
    # INT
    poor_count = scrapy.Field()
    # INT
    after_count = scrapy.Field()
    # FLOAT
    good_rate = scrapy.Field()
    # FLOAT
    general_rate = scrapy.Field()
    # FLOAT
    poor_rate = scrapy.Field()
    # 平均分FLOAT
    average_score = scrapy.Field()
    # TINYTEXT
    num = scrapy.Field()