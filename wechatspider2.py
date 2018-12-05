import requests
import time
import json,csv
"""
抓包软件爬微信公众号文章，不容易封的方法
爬取步骤
1。微信客户端打开历史文章，charles抓包，不断下滚翻下一页
2。抓包软件看见一个mp.weixin.qq.com不断变黄色，打开看里面的url
3。浏览器打开url就是，json包了
4。f12查headers拼接进来，url的offset从0开始翻页，0，11，21，31
参考：https://github.com/pythonchannel/spider_works/tree/master/%E5%85%AC%E4%BC%97%E5%8F%B7%E7%88%AC%E8%99%AB
"""


class mp_spider(object):

    def __init__(self):
        self.li = []
        self.offset = 0
        self.count = 0
        self.base_url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5NzI3NDg4MA==&f=json&offset=20&count=10&is_ok=1&scene=124&uin=MTc5NzUxMjM0MA%3D%3D&key=94f4a4917bbfd6eb461d9f5aa8f024110599a6e69dcfd72fa14ce301213e18517881ca1c58d2cece7fbdc7de7aad706a36cde33d82ad49f89a0dea156e00f09de705a15a1e9c86a07b4293472edb126e&pass_ticket=hvCRpWOU%2FTny4nf72ZRSuf14cQaFESs1fEeBmhaMrxhtAQfxTVnOZtS32sxFlkiJ&wxtoken=&appmsg_token=985_wXVINAHkUx6nhdmsUPj8Wqo9unuC3MOzZg22gw~~&x5=0&f=json'
        self.headers = {
            'Host': 'mp.weixin.qq.com',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Cookie': 'pgv_pvid=6751777100; sd_userid=85871542339048696; sd_cookie_crttime=1542339048696; pgv_pvi=1805300736; pt2gguin=o2442972114; RK=sPjsyLbxm6; ptcz=56838912653767a7f02cde6edf3f843004786c14270f8f3137cf852accde6186; wxuin=1797512340; pass_ticket=hvCRpWOU/Tny4nf72ZRSuf14cQaFESs1fEeBmhaMrxhtAQfxTVnOZtS32sxFlkiJ; devicetype=iMacMacBookPro81OSXOSX10.12.6build(16G29); version=12031210; lang=pt; rewardsn=; wxtokenkey=777; wap_sid2=CJS5j9kGElxPcTFUU2FVWVVFZTNfUDktMzBpNWFXVE0xZTVyZXlVampQN3ZtOTA3blpVa25sc0ZUMU55b01scFlrc3d4anMyYTN6XzV6bjAwcHNaWXhmcTE1MC1QZGtEQUFBfjCSlZ3gBTgNQJVO'
        }

    def request_data(self):
        response = requests.get(self.base_url.format(self.offset), headers=self.headers)
        if 200 == response.status_code:
            self.parse_data(response.text)

    def parse_data(self, response_data):

        all_datas = json.loads(response_data)

        if 0 == all_datas['ret']:
            if 1 == all_datas['can_msg_continue']:
                summy_datas = all_datas['general_msg_list']
                datas = json.loads(summy_datas)['list']
                for data in datas:
                    try:
                        title = data['app_msg_ext_info']['title']
                        title_child = data['app_msg_ext_info']['digest']
                        article_url = data['app_msg_ext_info']['content_url']
                        cover = data['app_msg_ext_info']['cover']
                        copyright = data['app_msg_ext_info']['copyright_stat']
                        copyright = '原创文章_' if copyright == 11 else '非原创文章_'
                        self.count = self.count + 1
                        print('第【{}】篇文章'.format(self.count), copyright, title, title_child, article_url, cover)
                        # 保存成csv
                        f = open('人民网.csv', 'w', encoding='utf-8-sig', newline='')
                        writer = csv.writer(f)
                        # 将一个个字段数据提取出来
                        # print(title)
                        t = (title, title_child, article_url,cover)
                        self.li.append(t)
                        # 列表格式 ：[('xxxx',), ('xxxx',)]
                        # print(self.li)
                        # writerows保存多行，格式是[('xxxx',), ('xxxx',)] writerow保存单行，格式['a','b']
                        writer.writerows(self.li)
                    except:
                        continue

                time.sleep(3)
                self.offset = all_datas['next_offset']  # 下一页的偏移量
                self.request_data()
            else:
                exit('数据抓取完毕！')
        else:
            exit('数据抓取出错:' + all_datas['errmsg'])




if __name__ == '__main__':
    d = mp_spider()
    d.request_data()