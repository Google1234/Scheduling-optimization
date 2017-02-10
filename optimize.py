# -*- coding: UTF-8 -*-
rlt_path=""
import config
import file
from pulp import *

def opt():
    A,B,candinates=file.get()
    #variable
    X=[LpVariable("x"+str(i),0,None,LpBinary) for i in range(len(candinates))]
    #optimize problem
    prob=LpProblem("schedule problem",LpMinimize)
    #constraint
    for i in range(len(B)):
        prob+=lpDot(A[i],X)>=B[i]
    #object
    obj=lpSum(X)
    prob+=obj
    #slove problem
    solution=prob.solve()
    #output result
    schedule=[]
    if LpStatus[solution]=='Optimal': #has optimal solution
        for i in range(len(X)):
            if value(X[i])==1:
                schedule.append(candinates[i])
        return schedule
    else:
        print u"错误：不存在调箱方案满足零件需求"

if __name__=='__main__':
    print opt()