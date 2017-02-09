from pulp import *
#variable
x1=LpVariable("x1",0,None,LpInteger)
x2=LpVariable("x2",0,None,LpInteger)
x3=LpVariable("x3",0,None,LpInteger)
x4=LpVariable("x4",0,None,LpInteger)
x5=LpVariable("x5",0,None,LpInteger)
x6=LpVariable("x6",0,None,LpInteger)
x7=LpVariable("x7",0,None,LpInteger)
x8=LpVariable("x8",0,None,LpInteger)
x9=LpVariable("x9",0,None,LpInteger)
x10=LpVariable("x10",0,None,LpInteger)
x11=LpVariable("x11",0,None,LpInteger)
x12=LpVariable("x12",0,None,LpInteger)
x13=LpVariable("x13",0,None,LpInteger)
#
prob=LpProblem("my",LpMinimize)
#constraint
a=[[0 for i in range(13)] for j in range(11)]
a[10][0]=900
a[0][1]=7800
a[0][2]=5000;a[4][2]=1000;a[6][2]=4160
a[7][3]=1344;a[8][3]=1338
a[2][4]=720
a[3][5]=720;a[7][5]=1000;a[8][5]=1000
a[0][6]=720;a[4][6]=720
a[4][7]=360
a[1][8]=10
a[4][9]=720
a[4][10]=360
a[9][11]=72
a[5][12]=1440
demand=[500,10,500,500,500,500,500,500,500,72,500]
b=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x3]
#print lpDot(a,b)
for i in range(11):
    prob+=lpDot(a[i],b)>=demand[i]
#obj
obj=sum(b)
prob+=obj
#solve
rst=prob.solve()
#result
print LpStatus[rst]
for k in b:
    print value(k)

