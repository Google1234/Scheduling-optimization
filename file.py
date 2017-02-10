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
    lists_data=pd.read_excel(rlt_path+config.input_file_lists)
except:
    print u"无文件：集装箱清单.XLSX"


print lists_data
boxs={}
components={}
searchs=set(names)
for row in range(len(lists_data)):
    try:
        if lists_data.iloc[row][0] in searchs:
            #print lists_data.iloc[row][0]
            component=lists_data.iloc[row][0]
            searchs.remove(component)
            components[component]=row
            line=lists_data.loc[component][:]
            print line


    except:
        print row
if searchs!=[]:
    for name in names:
        print u"错误：清单中无零件:",name
