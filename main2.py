import sys
from scipy.optimize import linprog as LP

p = [-20, -12, -40, -25]#since eqn is written as y + cx =0, to optimize y
ieq = [[1, 1, 1, 1], [3, 2, 1, 0], [0, 1, 2, 3]]
c = [50, 100, 90]

niBounds = (0, 50)

ans = LP(p, A_ub = ieq, b_ub = c, bounds = (niBounds, niBounds, niBounds, niBounds), options={"disp": False})

#the array represented by x will have the optimum values of ni
print(ans)