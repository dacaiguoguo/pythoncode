#!usr/bin/env python
# -*- coding: utf-8 -*-
# hanhan load

from base64 import encodestring
import sys 
def base64stringret(stringtobase):
	base64string = encodestring(stringtobase)
	print base64string
if __name__ == '__main__':  
	base64stringret(sys.argv[1])