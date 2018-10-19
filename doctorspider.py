import json

import requests
import csv,codecs
# import xlsxwriter
from lxml import etree

class MovieSpider(object):

    def __init__(self):
        self.url='http://www.dr-elephant.com/dclist.asp?page={}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        self.li=[]

    def get_page_from_url(self,url):
        """
        提取url
        :param url:
        :return:
        """
        html = requests.get(url, headers=self.headers).content
        return html

    def get_data_from_page(self,page):
        """
        提取数据
        :param page:
        :return:
        """
        s = etree.HTML(page)
        data_list=[]
        # 用xpath提取节点
        a_s = s.xpath("//div[@class='dccontentx']")
        for a in a_s:
            item={}
            item['doctor']=a.xpath("./h3/span/text()")[0]
            data_list.append(item)
        # print(data_list)
        return data_list

    def save_data(self,data_list):
        """
        保存数据
        :param data_list:
        :return:
        """
        for data in data_list:
            f = open('doct3.csv','w',encoding='utf-8-sig')
            writer = csv.writer(f)
            # 将一个个医院提取出来
            doctor=data['doctor']
            # print(doctor) 是一个个字符串
            t = (doctor,)
            self.li.append(t)
            # 列表格式 ：[('天津医科大学代谢病医院',), ('济南市第四人民医院',)]
            print(self.li)
            # writerows保存多行，格式是[('天津医科大学代谢病医院',), ('济南市第四人民医院',)] writerow保存单行，格式['a','b']
            writer.writerows(self.li)

    def run(self):
        for i in range(1, 21):
            # 获取url
            url=self.url.format(i)
            # 解析url
            page = self.get_page_from_url(url)
            # 获取数据
            data_list = self.get_data_from_page(page)
            # 保存数据为csv
            self.save_data(data_list)


if __name__ == '__main__':

    mm = MovieSpider()
    mm.run()

