"""
统计微信各种好友信息输出xls

"""
# coding:utf-8
import itchat,time,sys,xlwt

file = xlwt.Workbook()
table = file.add_sheet('info',cell_overwrite_ok=True)



# 登录-持续
itchat.auto_login()
print(u"logged")
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

table.write(0,5,u'【made by junzi】')
table.write(0,7,u'【共'+str(len(friends)-1)+u'位朋友，'+str(male)+u'位男性朋友，'+str(female)+u'位女性朋友，另外'+str(other)+u'位不明性别】')
table.write(0,0,u' 【昵称】')
table.write(0,1,u' 【备注名】')
table.write(0,2,u' 【省份】')
table.write(0,3,u' 【城市】')
table.write(0,4,u' 【签名】')

a=0

for i in friends:


    table.write(a+1,0,i['NickName'])
    table.write(a+1,1,i['RemarkName'])
    table.write(a+1,2,i['Province'])
    table.write(a+1,3,i['City'])
    table.write(a+1,4,i['Signature'])
    if i['RemarkName'] == u'':
        table.write(a+1,1,u'[ ]')
    if i['Province'] == u'':
        table.write(a+1,2,u'[ ]')
    if i['City'] == u'':
        table.write(a+1,3,u'[ ]')
    if i['Signature'] == u'':
        table.write(a+1,4,u'[ ]')



    a=a+1
    print(a)


# qm=raw_input("file name >>>:")
aaa='weixin_'+time.strftime("%Y%m%d", time.localtime())+'.xls'
file.save(aaa)
itchat.send('made by junzi','filehelper')
itchat.send('@%s@%s' % ('fil',aaa), 'filehelper')
print ("over")



