#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
str0 = r'sublime text <a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a></span>'
print(str0.encode('utf-8'))
atitle = str0.find(r'<a title=')
print(atitle)
href = str0.find(r'href=')
# print href
html = str0.find(r'.html')
# print html
url = str0[href + 6:html + 5]
print(url)

data = urllib.request.urlopen(url).read()
data = data.encode('UTF-8')
# print(httpResponse.code)
# print(httpResponse.info)
# blog =  httpResponse.read()
print(data)
