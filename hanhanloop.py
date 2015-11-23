#!usr/bin/env python
# -*- coding: utf-8 -*-
# hanhan load

import urllib2
from base64 import encodestring

request = urllib2.Request('https://api.github.com/user')
base64string = encodestring('%s:%s' % ('dacaiguoguo', '511guoguogit')).replace('\n', '')
request.add_header('Authorization', 'Basic %s' % base64string)
r = urllib2.urlopen(request)

print r.getcode()
print r.headers["content-type"]
print r.headers["X-RateLimit-Limit"]
print r.read()