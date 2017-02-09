from  pulp import *
import numpy

x1=LpVariable("x1",0,None,LpContinuous)
x2=LpVariable("x2",0,None,LpContinuous)
x3=LpVariable("x3",0,None,LpContinuous)
#
prob=LpProblem("my",LpMinimize)
#constraint

prob+=x1+x2+x3<=4
prob+=x1<=2
prob+=x3<=3
prob+=3*x2+x3<=6
#obj
obj=lpSum(-x1-14*x2-6*x3)
prob+=-x1-14*x2-6*x3
#slove
rst=prob.solve()
print LpStatus[rst] #important
print value(obj)


