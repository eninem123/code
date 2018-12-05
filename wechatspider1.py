# -*- coding: utf-8 -*-
import requests
import time
import csv
"""
微信公众号爬虫
需要提交的data
以下个别字段是否一定需要还未验证。
注意修改yourtoken,number
begin表示从第begin页开始爬取，为5的倍数，从0开始。如0、5、10……
token可以使用Chrome自带的工具进行获取
fakeid是公众号独一无二的一个id，等同于后面的__biz
参考：https://blog.csdn.net/wnma3mz/article/details/78570580
"""


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Host": "mp.weixin.qq.com",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=1862390040",
    "Cookie": "pgv_pvid=9498751209; pgv_pvi=428076032; RK=sPjsyLbhy6; ptcz=9859bf94715699d49e4a6a66b8c0d499cf5154865c8a114a0701f84e7d8baae6; o_cookie=2442972114; pac_uid=1_2442972114; ua_id=0yISQiLv4q7caT0BAAAAAK03YmkztOT6jPo1WZx2FDA=; mm_lang=zh_CN; noticeLoginFlag=1; _ga=GA1.2.1956877728.1541494631; pgv_si=s3467182080; cert=tPEtxRtBtxEVOdtKgSvvJttAj9P5tCum; master_key=P79GlwMcDCH8mTm9v0HinqJD1yl2MgrQLUgSJdX7U1c=; pgv_info=ssid=s4831455345; ptisp=cm; ptui_loginuin=1105499328; pt2gguin=o1105499328; uin=o1105499328; skey=@sbzf0jRRU; sig=h019d6b67ebaf8cd117a515adb82fc9d7f4208c13fff66d3fdebd77aa705aadd5e50cc08770ea07a7c0; uuid=7c6a0a76298cb2dce3a970e6aa0405c1; ticket=fd7eadf4120f0db64fdc431dbc5086b74cd40477; ticket_id=gh_0c2e05940f96; remember_acct=1105499328%40qq.com; data_bizuin=3240103118; bizuin=3268085583; data_ticket=dr6qgVEjHOGDrDTUP5lEmRfTRyCjOzvVRNAauMMCpkvlqCa21CVkF0AzUoa+MqEg; slave_sid=dlRYQ0xYdmFCczJxT3ZYNDJWTUdGVW9Qd0RTZEFFMUZjRkNsUEZIWWJ6TXBaTk5BQ0NmcHd0RjBFeFc3RDRnejk1aEJZVlhLbUJVMnVjWEl3REMyR3pOTFdJUFB1RElqbV9hR2ZDSEc2WF9vT0NhUVhLZWp3UGJGZ0RHdmk0enFMN0NpWXlBSlppVXdubFY0; slave_user=gh_0c2e05940f96; xid=4f0f831250e59fc989580c2eac5f3b8e; openid2ticket_ozgwgwduTYsDT5nndZC_6BVIArXw=VsyuVLTuTIi7OFhL06Bikut7OzsKmGHfBVs6kinZgvM="
}

for i in range(11):
    url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token=1687199925&lang=zh_CN&f=json&ajax=1&random=0.5124554479638495&action=list_ex&begin={}&count=5&query=&fakeid=MjM5NDYwMzUyMA%3D%3D&type=9".format(
        str(i * 5))
    print(i)
    #url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token=1862390040&lang=zh_CN&f=json&ajax=1&random=0.17794584803309532&action=list_ex&begin={}&count=5&query=&fakeid=&type=9".format(
     #   str(i * 5))

    response = requests.get(url, headers=headers)

    content_json = response.json()
    for item in content_json["app_msg_list"]:

    # 遍历 构造可存储字符串

        f = open('美年大健康.csv', 'a+', encoding='utf-8-sig', newline='')
        writer = csv.writer(f)
        li = []
        title = item["title"]
        url = item["link"]

        t = (title,url)

        li.append(t)
        print(li)
        writer.writerows(li)

