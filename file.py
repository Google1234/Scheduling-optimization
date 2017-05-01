# -*- coding: UTF-8 -*-
rlt_path=""
import pandas as pd
import xlrd
import config
import numpy as np

def get():
    #load demands from file
    try:
        demands_data=pd.read_excel(rlt_path+config.input_file_demand)
    except:
        print u"无文件：零件需求.XLSX"
        raise Exception

    B=demands_data[u"需求"].tolist()                                                                  ####B
    components=map(str,demands_data[u"零件号"].tolist()) #must change str,int,float to string

    #load lists from file
    try:
        lists_data = pd.read_excel(rlt_path + config.input_file_lists, header=3, index_col=0)
    except:
        print u"无文件：集装箱清单.XLSX"


    matrix=lists_data.loc[components].notnull()
    components_status=matrix.any(axis='columns')
    for component in components_status.index:
        if components_status[component]==False:
            print u"错误：集装箱清单中无零件",component
            raise Exception
    boxs_status=matrix.any(axis='index')
    boxs=[]
    for box in boxs_status.index:
        if boxs_status[box]==True and box!=u"总计":  #总计那一列为True，但并不是集装箱
            boxs.append(box)
    A=np.asarray(lists_data.loc[components][boxs].fillna(0))                                            ####A
    #print A,B,components
    return A,B,components,boxs

if __name__ == '__main__':
    A,B,components,boxs=get()
    print "matrix:",A
    print "demands:",B
    print "components", components
    print "candinate boxs:",boxs
