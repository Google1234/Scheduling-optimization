# -*- coding: UTF-8 -*-
import sys
try:
	rlt_path=""
	import config
	import optimize
	rst=optimize.opt()
	print u'结果：需要调的集装箱'
	print rst
except :
    print "Unexpected error:", sys.exc_info()[0]
raw_input('press enter to exit!')