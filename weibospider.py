"""
微博爬虫，输入某关键字就爬取对应用户
将微博名，关注数，粉丝数，微博数提取
"""
import requests
import csv,codecs
from bs4 import BeautifulSoup

class MovieSpider(object):

    def __init__(self):
        self.url='https://s.weibo.com/user?q=健康&Refer=weibo_user&page={}'
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
        data_list=[]
        soup = BeautifulSoup(page, 'html.parser')
        list_info = soup.find_all(class_="info")
        # item['wbname'] = wbname
        for list in list_info:
            # print(list)
            # 格式都是字符串
            item={}
            item['wbname'] = list.find(class_="name").text
            item['focus'] = list.select('span')[0].a.get_text()
            item['follow'] = list.select('span')[1].a.get_text()
            item['weibo'] = list.select('span')[2].a.get_text()
            data_list.append(item)
        print('data_list',data_list)
        return data_list

    def save_data(self,data_list):
        """
        保存数据
        :param data_list:
        :return:
        """
        for data in data_list:
            # print(data)
            f = open('weibo.csv','w',encoding='utf-8-sig')
            writer = csv.writer(f)
            # 将微博名，关注数，粉丝数，微博数提取，转成写入格式
            wbname=data['wbname']
            follow=data['follow']
            focus=data['focus']
            weibo=data['weibo']

            # print('follow:',follow) # 是一个个字符串
            t = (wbname,focus,follow,weibo)
            self.li.append(t)
            # 列表格式 ：[('xxx',), ('xxx',)]
            # print('list:',self.li)
            # writerows保存多行，格式是[('xxx',), ('xxxx',)] writerow保存单行，格式['a','b']
            writer.writerows([['微博名','关注数','粉丝数','微博数']])
            writer.writerows(self.li)

    def run(self):
        for i in range(1, 50):
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

