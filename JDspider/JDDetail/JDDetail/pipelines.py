# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter
import pymysql


class JDDetailPipeline(object):

    def __init__(self):

        self.settings = get_project_settings()
        self.connect = pymysql.connect(
            host=self.settings['MYSQL_HOST'],
            port=self.settings['MYSQL_PORT'],
            db=self.settings['MYSQL_DBNAME'],
            user=self.settings['MYSQL_USER'],
            passwd=self.settings['MYSQL_PASSWD'],
            charset=self.settings['MYSQL_CHARSET'],
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

            sql = 'insert into jingdong.JDDetail(name,price,owner,flag,comment_count,good_count,default_good_count,' \
                  'general_count,poor_count,after_count,good_rate,general_rate,poor_rate,average_score,num,jd_sel,global_buy)'\
                  'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            self.cursor.execute(sql, (item['name'], item['price'], item['owner'], item['flag'], item['comment_count'],
                                      item['good_count'], item['default_good_count'], item['general_count'],
                                      item['poor_count'], item['after_count'], item['good_rate'], item['general_rate'],
                                      item['poor_rate'], item['average_score'], item['num'], item['jd_sel'], item['global_buy']))
            print("mysql商品详情信息插入成功")
            self.connect.commit()

    def close_spider(self, spider):
        # 关闭mysql
        self.cursor.close()
        self.connect.close()


class JDDetailCsvPipeline(object):
    """保存为CSV格式文件的管道类"""
    def open_spider(self,spider):
        # 保存csv数据库文件对象
        self.f = open("jddetail.csv", "wb")
        # 创建csv文件读写对象
        self.csv_exporter = CsvItemExporter(self.f)
        # 开始进行csv文件的读写
        self.csv_exporter.start_exporting()

    def process_item(self,item,spider):
        # 每次写入一个item数据
        print(type(item))
        print(item)
        #print(chardet.detect(list(dict(item).values())[0]))
        print("--" * 50)
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 结束csv文件读写
        self.csv_exporter.finish_exporting()
        # 关闭文件
        self.f.close()