"""
微信群呢称爬取
"""
import itchat, time



itchat.auto_login(enableCmdQR=False)
# 获取群
roomslist = itchat.get_chatrooms()
# 群名称
itchat.dump_login_status()  # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
myroom = itchat.search_chatrooms(name='xx群')  # 群聊名称
gsq = itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)

# 保存
with open('gss1.txt', 'a') as f:
    for c in gsq['MemberList']:
        print(c['NickName'] + ":" + c['DisplayName'] + '\n')
        f.write(c['NickName'] + '\n')
