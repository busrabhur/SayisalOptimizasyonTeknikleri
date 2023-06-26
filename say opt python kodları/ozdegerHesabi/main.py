
import numpy as np
from numpy.linalg import  eig

#matris-->hessian matrisinin özdeğerlerini incelicez
A=np.array([[3,2],[2,1]]) #bunu alt alta matris gibi hayal et 4x4 lük
w,v=eig(A) #w içinde özdeğerler var , v içinde özvektörler var
print(w)  #bizim ilgilendiğimiz kısım özdeğerler (w)

#w--> matrisin özdeğerlerini verecek.özdeğerlerin hepsi pozitifse kesin yerel minimum noktası kararı verilir.
# özdeğerlerin biri pozitif biri negatif vs ise semer noktasıdır.Özdeğerler negatifse yerel maxtır.




