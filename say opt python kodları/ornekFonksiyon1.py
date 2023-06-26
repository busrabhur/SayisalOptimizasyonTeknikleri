import numpy as np
import math 

def f(xk): #fonknun kendsi
    x1=xk[0]
    x2=xk[1]
    fk=3+(x1-1.5*x2)**2+(x2-2)**2
    return fk

def gradient(xk):
    x1=xk[0]
    x2=xk[1]
    gk=np.array([2*(x1-1.5*x2), -3*(x1-1.5*x2)+2*(x2-2)])
    return gk

def hessian(xk): # SD yöntemi hessian kullanmıyo boşuna yazma
    x1=xk[0]
    x2=xk[1]
    Hk=np.matrix([[2, -3],[-3, 6.5]])
    return Hk

def error(xk): #---erroru bulduktan sonra jacobianı bulmak çok kolay
    x1=xk[0]
    x2=xk[1]
    ek=np.array([np.sqrt(3),(x1-1.5*x2),(x2-2)])
    return ek

def jacobian(xk): #1.satır:error vektörünün önce 1. elemanının türevini x1 ve x2 ye göre sırayla al tüm satırlar aynı mantık
    x1=xk[0]
    x2=xk[1]
    Jk=np.matrix([[0,0],[1,-1.5],[0,1]])
    return Jk
    