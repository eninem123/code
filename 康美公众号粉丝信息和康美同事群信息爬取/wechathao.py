"""
获取微信公众号粉丝呢称信息和微信群信息整理成数据集功能
"""
import requests
import json
import csv
import itchat
import time
import os
import numpy as np
import pandas as pd
class wechatspider():

    def __init__(self):

        # 连接公众号获取token
        token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx488078f27e37a708&secret=b2244d70ebbd7f3403db939b95c0e2f2"
        token = requests.get(url=token_url)
        # 得到的是bytes字节
        print(token.content)
        content = token.content.decode('utf8')
        # 得到json字符串，转成字典
        content = json.loads(content)
        print('content', content)
        print('contenttype:', type(content))
        self.access_token = content['access_token']
        print('access_token', self.access_token)
        print('access_tokentype:', type(self.access_token))

        # 对粉丝列表发起请求
        guanzhu_url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={}".format(self.access_token)

        # 返回用户列表
        user_list = requests.post(url=guanzhu_url).content.decode('utf8')
        print("res", user_list)
        print("restype:", type(user_list))
        self.user_dict = json.loads(user_list)

    def spiderqun(self):
        # 登陆微信获取群
        itchat.auto_login(enableCmdQR=False)
        # 获取群
        roomslist = itchat.get_chatrooms()
        # 群名称
        itchat.dump_login_status()  # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
        myroom = itchat.search_chatrooms(name='健康产业同事群')  # 群聊名称
        gsq = itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)
        # print(gsq)
        # print(type(gsq))

        with open('微信公众号粉丝信息和群信息.csv', 'a+', encoding='utf-8-sig', newline='') as f:
            csv_writer = csv.writer(f)
            for c in gsq['MemberList']:
                qunuser = c['NickName']
                csv_writer.writerow([qunuser])

    def spiderhao(self):
        # 根据用户列表得到性别等信息，保存到csv
        with open('微信公众号粉丝信息和群信息.csv', 'a+', encoding='utf-8-sig', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['nickname', 'sex', 'city', 'province', 'country','wechatqun'])
            for i in self.user_dict["data"]["openid"]:
                user_url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN".format(
                    self.access_token, i)
                # windows系统要加decode() linux系统不需要
                res_user = requests.get(user_url).content.decode()
                print(res_user)
                print(type(res_user))
                res_user = json.loads(res_user)
                nickname = res_user["nickname"]
                sex = str(res_user["sex"])
                city = res_user["city"]
                province = res_user["province"]
                country = res_user["country"]
                # print(nickname + '\n')
                # print('country:',type(country))
                # print('country:',country)
                # 保存


                csv_writer.writerow([nickname, sex, city, province, country])
                # f.write(nickname + '\n')

    def fixcsv(self):
        # 将微信号和微信群的信息整理合并
        df = pd.read_csv('./微信公众号粉丝信息和群信息.csv')
        # 找到公众号和微信得分界处得那个人名称
        index_name = df.iloc[1, 0]
        data = df.loc[df["nickname"] == index_name]
        index = data.index[1]
        # 将nickname列按照分界线将下面的数据剪切到wechatqun列
        df["wechatqun"] = df["nickname"].shift(-index)
        # 原来的数据删了
        df.loc[index:, ("nickname")] = np.nan
        df.to_csv('微信公众号粉丝信息和群信息.csv', encoding='utf-8-sig', index=False)

    def batchrename(self):
        filename = '微信公众号粉丝信息和群信息.csv'
        newname = '微信公众号粉丝信息和群信息.xls'
        os.rename(filename, newname)


if __name__ == '__main__':
    s = wechatspider()
    s.spiderhao()
    s.spiderqun()
    s.fixcsv()
    s.batchrename()