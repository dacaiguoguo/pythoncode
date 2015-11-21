#!/usr/bin/env python
#coding:utf-8
#while 循环－－－－－－－－－－
x = 1
while x <= 2:
    print x
    x += 1
    
#for 循环－－－－－－－－－－－ 注意最后的：一定要加
words = ['this','is','an', 'ex', 'parrot']
for word in words:
    print word
# range 函数创建数组，包含前，不包含后
numbers = range(2,5)
for number in numbers:
    print number
# 创建字典的方法注意
d = {'z':1, 'a':2, 'b':3}
for key in d:
    print key, 'corresponds to' , d[key]
# items 将字典返回成键值对的元组数组，顺序是不确定的
for key, value in d.items():
    print key, 'corresponds to', value

# 十六进制 ？？怎么表示负数呢？
print 0xaf
# 八进制

print x*10
# get user input
# x = input("x:")
# y = input("y:")
# # get 求幂的两种方法
# print x**y
# print pow(x,y)
import math
print int(math.floor(32.9))
#列表 和 index 方法
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'We', 'are']
indexofwho = knights.index('who')
print knights[indexofwho]
#列表的count 方法 用于统计某元素在列表中出现的次数
print knights.count('are')
#extend 方法 可以在列表末尾添加另一个列表中的多个值，就是扩展原有的列表
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print a
# 注意和+连接不同，连接方法是创建新的列表，而extend 是修改了列表内容
print a+b
print 'a = %s' % a 
#也可以用分片赋值的方法
print 'fen pian'
b = ['a','b','c']
a[len(a):] = b
print a
eggs_list = [1, 2, 3]
eggs_list.append('eggs')
print eggs_list

#list 函数 然后可以用 ''.join() 的方法把它拼接回来
stringList = list('Hello list funtioi')
print stringList.count('t')
print '----------'
#注意求列表长度用的是len() 分片赋值 直接用-5就可以，
#在python中 最后一个元素是系上-1个，以此类推
stringList[len(stringList)-5:] = 'n!'
print ''.join(stringList)
print a
a[3:-2] = []
print 'qie pian delete %s' % a
# 删除操作
del a[0]
print a
#分片步长
number = range(1,17)
print number[::2]
print number[1::2]
print number[::-2]
#建立空列表
print [None]*10
print 't' in stringList
print stringList.count('t')














