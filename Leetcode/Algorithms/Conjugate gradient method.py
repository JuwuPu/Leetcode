import numpy as np


A = np.array([4,-1,1,-1,4,-2,1,-2,4]).reshape(3,3)
b = np.array([12,-1,5]).reshape(3,1)

def conjugatGradient(A, b, x, epsilon = 0.005):
    x = x.reshape(np.shape(b))
    r = b - np.dot(A, x).reshape(np.shape(b))
    rho = sum(r*r)
    p = r

    while(rho > epsilon):
        w = np.dot(A, p).reshape(np.shape(b))
        alpha = rho / sum(p*w)
        x = x + alpha*p
        r = r - alpha*w
        rho_new = sum(r*r)
        beta = rho_new / rho
        p = r + beta*p
        rho = rho_new



    return x

conjugatGradient(A,b,x=np.zeros(3))
