# -*- coding: UTF-8 -*-
rlt_path = ""
import config
import file
from pulp import *
import os


def getNotEnoughComponent(A, B, components):
    sum_A = []
    for i in range(0, len(A)):
        item_A = A[i]
        sum = 0
        for j in range(0, len(item_A)):
            sum += item_A[j]
        sum_A.append(sum)
    new_A = []
    new_B = []
    new_components = []
    not_enough = []
    not_enough_A = []
    not_enough_B = []
    for i in range(0, len(sum_A)):
        # have < need
        if (sum_A[i] < B[i]):
            not_enough.append(components[i])
            not_enough_A.append(A[i])
            not_enough_B.append(B[i])
        else:
            new_A.append(A[i])
            new_B.append(B[i])
            new_components.append(components[i])
    return new_A, new_B, new_components, not_enough, not_enough_A, not_enough_B


def opt():
    A, B, components, candinates = file.get()

    A, B, components, not_enough, not_enough_A, not_enough_B = getNotEnoughComponent(A, B, components)
    if (len(not_enough) > 0):
        print u"以下得零件不足："
        for i in range(0, len(not_enough)):
            print "零件" + str(not_enough[i]) + "需求:" + str(not_enough_B[i]) + "\n",
            sum = 0
            for j in range(0, len(not_enough_A[i])):
                if (not_enough_A[i][j] > 0):
                    print str(candinates[j]) + ":" + "数量"+str(not_enough_A[i][j]) + ',',
                    sum += not_enough_A[i][j]
            print "\n共计:" + str(sum)
            print "差额:" + str(not_enough_B[i]-sum)

    # variable
    X = [LpVariable("x" + str(i), 0, None, LpBinary) for i in range(len(candinates))]
    # optimize problem
    prob = LpProblem("schedule problem", LpMinimize)
    # constraint
    for i in range(len(B)):
        prob += lpDot(A[i], X) >= B[i]
    # object
    obj = lpSum(X)
    prob += obj

    # slove problem
    cwd = os.getcwd()
    solverdir = 'Cbc-2.7.5-win64-intel11.1\\bin\\cbc.exe'  # extracted and renamed CBC solver binary
    solverdir = os.path.join(cwd, solverdir)
    solver = pulp.COIN_CMD(path=solverdir)
    solution = prob.solve(solver)
    # output result
    schedule = []
    if LpStatus[solution] == 'Optimal':  # has optimal solution
        for i in range(len(X)):
            if value(X[i]) == 1:
                schedule.append(candinates[i])
        return schedule
    else:
        print u"错误：不存在调箱方案满足零件需求"


if __name__ == '__main__':
    print opt()
