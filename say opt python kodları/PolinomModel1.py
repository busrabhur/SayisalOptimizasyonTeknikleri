import numpy as np
import math
from dataset1 import ti,yi
#-------------------------
def polinomIO(t,x):
    yhat=[ x[0] + x[1]*ti +x[2]*ti**2 for ti in t ]
    return yhat
#---------------------
numofdata=len(ti)
J=-np.ones((numofdata,1))
J=np.hstack((J, -np.ones((numofdata,1))*np.array(ti).reshape(numofdata,1)))
J=np.hstack((J, -np.ones((numofdata,1))*np.array(ti).reshape(numofdata,1)**2))
A=np.linalg.inv(J.transpose().dot(J))
B=J.transpose().dot(yi)
x=-A.dot(B)
T=np.arange(-3,3,0.1) #---hangi sayıların arasında çizdirmek istiyosun 0.1 a
yhat=polinomIO(T,x)
#-------------------------
import matplotlib.pyplot as plt
#plotting the points
plt.scatter(ti, yi, color='darkred',marker='x')
plt.plot(T, yhat, color='green', linestyle='solid' ,linewidth=1)
plt.xlabel('ti')
plt.ylabel('yi')
plt.title('polinom modeli',fontstyle='italic')
plt.grid(color='green' ,linestyle='--', linewidth=0.1)
plt.legend(['polinom modeli','gerçek veri'])
plt.show()
