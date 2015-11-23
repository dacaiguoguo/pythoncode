#usr/bin/env python
# -*- coding: utf-8 -*-
#cocoa m title load
import urllib
import urllib.request
import html

def loadOnePage(urlString):
	data = urllib.request.urlopen(urlString).read()
	href = r'p class="title"><a href="'
	data = data.decode('UTF-8')
	hreflocation = data.find(href)
	kk = 0
	ll = 0
	i=2
	while hreflocation != -1:
		ll = data.find(r'">',hreflocation)
		ll = data.find(r'">',ll+2)
		link = 'http://www.cocoachina.com/cms/' + html.unescape(data[hreflocation+25:ll])
		print(link)
		if i==2:
			linkrdata = urllib.request.urlopen(link).read()
			linkrdata = linkrdata.decode('UTF-8')
			print(linkrdata)
			i=1
		kk = data.find(r'</a></p>',ll+2)
		print(data[ll+2:kk])
		hreflocation = data.find(href,kk+2)

if __name__ == "__main__":
	for x in range(2)[1:]:
		print(x)
		sss =  'http://www.cocoachina.com/cms/wap.php?action=more&page=%s&more=1&page=%s' % (x, x)
		print(sss)
		loadOnePage(sss)

