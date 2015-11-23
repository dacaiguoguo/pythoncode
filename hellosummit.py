#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Url
#
import urllib2

def fetch(url):
    http_header = {'User-Agent': 'chrome'}
    http_request = urllib2.Request(url, None, http_header)
    
    print 'Start downloading data ...'
    http_response = urllib2.urlopen(http_request)
    print 'Finish downloading data'
    
    # Status Code
    print http_response.code
    print http_response.info()
    print "_____________data_____________"
    toprint =  http_response.read()
    print toprint
    print "_____________data over_____________"
    
if __name__ == "__main__":
    fetch(r"http://api.union.meituan.com/data/api?city=北京&category=美食&limit=10&district_name=朝阳区&key=4935ad94ae4e766f8fb37961a9627d3f148&keyword=火锅&sort=1")

    
