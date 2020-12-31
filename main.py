import sys
import pulp as p

prob = p.LpProblem('Analysis', p.LpMaximize)

n1 = p.LpVariable('n1', lowBound = 0, cat = 'Integer')
n2 = p.LpVariable('n2', lowBound = 0, cat = 'Integer')
n3 = p.LpVariable('n3', lowBound = 0, cat = 'Integer')
n4 = p.LpVariable('n4', lowBound = 0, cat = 'Integer')

prob += 20 * n1 + 12 * n2 + 40 * n3 + 25 * n4

prob += 3 * n1 + 2 * n2 + 1 * n3 <= 100
prob += 1 * n2 + 2 * n3 + 3 * n4 <= 90
prob += 1 * n1 + 1 * n2 + 1 * n3 + 1 * n4 <= 50

print(prob)

status = prob.solve()

print(p.LpStatus[status])

print(p.value(n1), p.value(n2), p.value(n3), p.value(n4))
print(p.value(prob.objective))