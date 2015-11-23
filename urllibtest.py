#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Url
#
#encoding:UTF-8
import urllib.request
import urllib

query = {}
query['word'] = 'jec'
url_values = urllib.parse.urlencode(query)
url = 'http://www.baidu.com/s?'
full_url = url+url_values
print(full_url)
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data[:20])