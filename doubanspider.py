from lxml import etree
import requests

#获取页面地址
def getUrl():
    for i in range(1):
     url = 'https://music.douban.com/top250?start={}'.format(i*25)
     scrapyPage(url)


#爬取每页数据
def scrapyPage(url):
    html = requests.get(url).content
    # print(html)
    s = etree.HTML(html)
    # print(s)
    trs = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')
    # print(trs)
    for tr in trs:
        href = tr.xpath('./td[2]/div/a/@href')[0]
        title = tr.xpath('./td[2]/div/a/text()')[0]
        score = tr.xpath('./td[2]/div/div/span[2]/text()')[0]
        number = tr.xpath('./td[2]/div/div/span[3]/text()')[0]
        img = tr.xpath('./td[1]/a/img/@src')[0]
        print(href, title, score, number, img)

if  '__main__':
    getUrl()