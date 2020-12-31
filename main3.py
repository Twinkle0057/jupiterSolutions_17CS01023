import sys
from gekko import GEKKO


#using direct equations
m = GEKKO()

n1 = m.Var(lb = 0, ub = 50)
n2 = m.Var(lb = 0, ub = 50)
n3 = m.Var(lb = 0, ub = 50)
n4 = m.Var(lb = 0, ub = 50)

m.Maximize(20 * n1 + 12 * n2 + 40 * n3 + 25 * n4)
m.Equation(3 * n1 + 2 * n2 + 1 * n3 <= 100)
m.Equation(1 * n2 + 2 * n3 + 3 * n4 <= 90)
m.Equation(1 * n1 + 1 * n2 + 1 * n3 + 1 * n4 <= 50)

m.solve()

print('Values of ni are: ', n1[0], n2[0], n3[0], n4[0])

print('Profit: ', 20 * n1[0] + 12 * n2[0] + 40 * n3[0] + 25 * n4[0])