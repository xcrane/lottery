#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
从2013年河北快3数据库中找出持续时间最长的大或者小
'''
import xlrd
book = xlrd.open_workbook('hbk3.xls')  # 打开Excel文件

print(book.nsheets)  # 读取Excel中的表单数

# 读取Excel中表单的名称

for aa in range(book.nsheets):
    sheet = book.sheet_by_index(aa)
    print(sheet.name)

# 打开某一个表单,并获取表单的名称
sheet1 = book.sheet_by_index(0)  # 打印index为0的sheet的名称
print(sheet1.name)

nrows = sheet1.nrows
ncols = sheet1.ncols
print(nrows)  # 打印sheet1的总行数
print(ncols)  # 打印sheet1的总列数

a1 = sheet1.cell(1, 2).value
# print(type(a1))

value = 0
FlagBig = False
FlagSmall = False
CountBig = 0
CountSmall = 0
CountMax = 0
LineNum = 0
for i in range(1, nrows):
    value1 = sheet1.cell(i, 2).value
    value2 = sheet1.cell(i, 3).value
    value3 = sheet1.cell(i, 4).value
    value = value1 + value2 + value3
    if value < 11:
        FlagSmall = True
        FlagBig = False
    else:
        FlagSmall = False
        FlagBig = True

    if FlagBig:
        CountBig = CountBig + 1
        CountSmall = 0
        if CountMax < CountBig:
            CountMax = CountBig
            LineNum = i

    if FlagSmall:
        CountSmall = CountSmall + 1
        CountBig = 0
        if CountMax < CountSmall:
            CountMax = CountSmall
            LineNum = i

print("CountMax is %d." % CountMax)
print("The last line of max num : %d." % (LineNum + 1))
