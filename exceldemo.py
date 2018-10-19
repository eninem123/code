import xlrd, xlwt

"""
读取excel
"""
data = xlrd.open_workbook('excel_file.xlsx')
table = data.sheets()[0]  # sheet页签
print(table)
print(table.nrows)  # 行
print(table.ncols)  # 列

for k in range(table.nrows):
    print(table.row_values(k))  # ['品牌', 'size', '价格', '性别']

for i in range(table.ncols):
    print(table.col_values(i))  # ['性别', '男', '女']
# text:'品牌'
print(table.cell(0, 0))  # 获取单元格数据，前一个是行数，从0开始，后一个是列数，且列数从0开始

for a in range(1, table.nrows):  # 行数据，我正好要去掉第1行标题
    for b in range(table.ncols):
        print(table.cell(a, b).value)
    print('----------------------')

"""
写入excel
"""
workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 其实就是execl，
worksheet = workbook.add_sheet('my_worksheet')  # 创建表，如果想创建多个，直接在后面再add_sheet
worksheet.write(0, 0, label='Row 0,Column 0 Value')  # 3个参数，第一个参数表示行，从0开始，第二个参数表示列从0开始，第三个参数表示插入的数值
workbook.save('execl_liu.xlsx')  # 写完记得一定要保存


