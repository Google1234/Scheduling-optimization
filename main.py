# -*- coding: UTF-8 -*-
import sys
try:
	rlt_path=""
	import config
	import optimize
	rst=optimize.opt()
	print u'调以下集装箱可以获取除数量不足的零件:'
	print rst
except :
    print "Unexpected error:", sys.exc_info()[0]
raw_input('press enter to exit!')
