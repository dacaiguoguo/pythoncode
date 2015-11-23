#!usr/bin/env python
# -*- coding: utf-8 -*-
# hanhan load
import re
import sys 
import json

def jsonzhuan(stringtobase):
	di = stringtobase
	print json.dumps(di, indent=4)
	# strinfo = re.compile('"')
	# print '=======================\n'
	# base64string = strinfo.sub(r'\"',stringtobase)
	# print base64string
if __name__ == '__main__':
	# jsonzhuan(sys.argv[1])
	jsonzhuan(r'''{"code":"1","data":{"count":0,"extra":"","hasNext":false,"list":[{"count":753,"queryType":"待审核"},{"count":8,"queryType":"待支付"},{"count":3,"queryType":"待出行"},{"count":187,"queryType":"待点评"},{"count":0,"queryType":"退款"},{"count":3,"queryType":"电子票"},{"count":36,"queryType":"优惠券"}],"suppChildOnSaleFlag":false},"errorMessage":"","message":"","version":"38e5af7f0a89f341b21748b219c9cddc"}''')