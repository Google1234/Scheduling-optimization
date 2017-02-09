# -*- coding: UTF-8 -*-
rlt_path=""
import pandas as pd
import xlrd
import config

#load demands from file
try:
    demands_data=pd.read_excel(rlt_path+config.input_file_demand)
except:
    print u"无文件：零件需求.XLSX"
    raise Exception
B=demands_data[u"需求"].tolist()
names=demands_data[u"零件号"].tolist()
length=len(B)
#load lists from file
try:
    lists_data=pd.read_excel(rlt_path+config.input_file_lists,index_col=None)
except:
    print u"无文件：集装箱清单.XLSX"

candidates=set()


a=lists_data.iloc[10][0]

print lists_data.loc[a]
