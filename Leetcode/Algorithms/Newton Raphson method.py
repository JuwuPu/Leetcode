### Bonus question for extra credit
##

def f(r, A = 1e4, M = 250, n = 60):
    return A*r - M * (1 - 1/(1 + r)**n)

def df(r, A = 1e4, M = 250, n = 60):
    return A - M * n / (1 + r)**(n + 1)

def newtonRaphson(r, tol=1.0e-9):
    r_old = r
    r = r_old - f(r_old) / df(r_old)
    while (abs(r - r_old) >= tol):
        r_old = r
        r = r_old - f(r_old) / df(r_old)
    return r

for r in range(101):
    r = r / 10
    print(newtonRaphson(r))