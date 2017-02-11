# -*- coding: UTF-8 -*-
try:
	rlt_path=""
	import config
	import optimize

	print u'结果：需要调的集装箱'
	print optimize.opt()
except:
	print u'无解！'
raw_input('press enter to exit!')