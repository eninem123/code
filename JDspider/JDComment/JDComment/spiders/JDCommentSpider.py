# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.utils.project import get_project_settings
from JDComment.items import JDCommentItem
import re
import json
import scrapy


class JdcommentspiderSpider(RedisSpider):
    name = 'JDCommentSpider'
    allowed_domains = ['www.jd.com']
    redis_key = 'JDCommentSpider:start_urls'

    settings = get_project_settings()
    comment_url = settings['COMMENT_URL']

    def parse(self, response):
        try:
            comment_json = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            return

        good_number = re.findall(r'productId=(\d+)', response.url)[0]
        max_page_num = comment_json['maxPage']

        for com in comment_json['comments']:
            item = JDCommentItem()
            item['good_num'] = good_number
            item['content'] = com['content']
            yield item

        for i in range(2, 4):
            yield scrapy.Request(self.comment_url.format(good_number, i), callback=self.get_leftover)

    def get_leftover(self, response):
        try:
            comment_json = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            return

        good_number = re.findall(r'productId=(\d+)', response.url)[0]

        for com in comment_json['comments']:
            item = JDCommentItem()
            item['good_num'] = good_number
            item['content'] = com['content']
            yield item

