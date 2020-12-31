We use linear programming to solve the inequations and equations

p1 = {Profit:= 20, CPU cost:= 3, GPU cost:= 0}
p2 = {Profit:= 12, CPU cost:= 2, GPU cost:= 1}
p3 = {Profit:= 40, CPU cost:= 1, GPU cost:= 2}
p4 = {Profit:= 25, CPU cost:= 0, GPU cost:= 3}

Total CPU available:= 100
Total GPU available:= 90

Total number of customers:= 50

i be product number
pi be profit
xi be cpu cost
yi be gpu cost
ni be number of customers

=> n1+n2+n3+n4 <= 50 inequality is because there may no CPU and GPU time available for remaining customers
=> 3n1+2n2+n1 <=100
=> n2+2n3+3n4 <=90

ni >= 0 Can't be negetive customers

P be total profit

P = 20n1+12n2+40n3+25n4

Maximizing P is our job

the above eqns can be written as(in matrix form):
    _  _        _  _        _  _        _  _        _   _
    | 1 |       | 1 |       | 1 |       | 1 |       | 50 |
 n1 | 3 | + n2  | 2 | + n3  | 1 | + n4  | 0 |   <=  | 100|
    |_0_|       |_1_|       |_2_|       |_3+|       |_90_|
    
Lets use library called PuLP(LP modeler for python) => main.py
there is another solution using scipy.optimize.linprog (Linear Programming in SciPy by using Dense matrices) => main2.py
and another one using GEKKO from gekko library (We can use both readable equations and inequations for solving and also Dense matrices of GEKKO to solve this problem just as in ) => main3.py

find the screenshots of the output in the same folder named respectively with the name of the file