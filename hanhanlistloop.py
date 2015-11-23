#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Url
#
import urllib2
import os

def fetch(str0):
	http_header = {'User-Agent':'Chrome'}
	http_request = urllib2.Request(str0, None, http_header)
	http_response = urllib2.urlopen(http_request)
	content = http_response.read()
	location =0
	href = 0
	html = -5
	i = 0
	while location != -1:
		location = content.find('<a title=',html + 5)
		href = content.find(r'href=',location)
		html = content.find(r'.html',href)
		url = content[href + 6:html + 5]
 		filename = os.path.split(url)[1]
 		if len(filename) > 1:
 			print filename
			f = open('/Users/sunyanguo/Desktop/Lvmm/'+filename, 'w')
			http_request = urllib2.Request(url, None, http_header)
			f.write(urllib2.urlopen(http_request).read())
			f.close()
		i = i+1
	print i
if __name__ == "__main__":
	for x in xrange(1,8):
		fetch(r"http://blog.sina.com.cn/s/articlelist_1191258123_0_"+str(x)+'.html')

