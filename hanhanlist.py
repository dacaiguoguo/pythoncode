#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Url
#
import urllib2
import urllib

# def findurl(content):
# 	location = content.find('<a title="')
# 	href = content.find(r'href=',location)
# 	html = content.find(r'.html',href)
# 	url = content[href + 6:html + 5]
# 	print url
# 	print content[html+5:]
# 	findurl(content[1:100])
# 	if len(content[html+5:]) > 10:
# 		findurl(content[html+5:])
import urlparse
import os
def fetch(str0):
	http_header = {'User-Agent':'Chrome'}
	http_request = urllib2.Request(str0, None, http_header)
	http_response = urllib2.urlopen(http_request)
	content = http_response.read()
	location = content.find('<a title="')
	href = content.find(r'href=',location)
	html = content.find(r'.html',href)
	url = content[href + 6:html + 5]
	print url
	i = 1

	while location != -1:
		location = content.find('<a title=',html + 5)
		href = content.find(r'href=',location)
		html = content.find(r'.html',href)
		url = content[href + 6:html + 5]
		# print url
		i = i+1
	print i
if __name__ == "__main__":
	fetch(r"http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html")

