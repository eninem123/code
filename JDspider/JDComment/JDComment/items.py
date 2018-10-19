# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDCommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # TINYTEXT
    good_num = scrapy.Field()
    # TEXT
    content = scrapy.Field()
