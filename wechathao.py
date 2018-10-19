"""
获取微信公众号粉丝呢称信息功能
"""
import requests
import json
import csv

# 获取token
token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=xxxx&secret=xxxb95c0e2f2"
token = requests.get(url=token_url)
# 得到的是bytes字节
print(token.content)
content = token.content.decode('utf8')
# 得到json字符串，转成字典
content = json.loads(content)
print('content', content)
print('contenttype:', type(content))
access_token = content['access_token']
print('access_token', access_token)
print('access_tokentype:', type(access_token))

# 对粉丝列表发起请求
guanzhu_url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={}".format(access_token)

# 返回用户列表
user_list = requests.post(url=guanzhu_url).content.decode('utf8')
print("res",user_list)
print("restype:", type(user_list))
user_dict = json.loads(user_list)
# 根据用户列表得到呢，性别等信息，保存到csv
for i in user_dict["data"]["openid"]:
    user_url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}&lang=zh_CN".format(access_token,i)
    res_user = requests.get(user_url).content
    res_user = json.loads(res_user)
    print(res_user)
    nickname = res_user["nickname"]
    sex = str(res_user["sex"])
    city = res_user["city"]
    province = res_user["province"]
    country = res_user["country"]
    # print(nickname + '\n')
    # print('country:',type(country))
    # print('country:',country)
    # 保存
    with open('fensi_info.xlsx', 'a',encoding='utf-8-sig') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow([nickname, sex, city, province, country])

        # f.write(nickname + '\n')