import math
import numpy as np

#bu kodu istenen fonksiyonu ve başlangç noktalarını xalt xüst değiştirerek istediğin problem için kullanabilirsin.

def f(x):
    f = (x-1)**2*(x-2)*(x-3)
    return f

xalt=0
xust=4

dx=0.0001 #sapma(hata payı) ne kadar olmasını istediğimizi bu şekilde belirtiriz.
alpha=(1+math.sqrt(5))/2
tau=1-1/alpha
epsilon=dx/(xust-xalt)
N=round(-2.078*math.log(epsilon))  #iterasyon sayısının tamsayı çıkması gerektğinden yuvarlama yaptık

x1=xalt+tau*(xust-xalt); f1=f(x1);
x2=xust-tau*(xust-xalt); f2=f(x2);

print(0,x1,x2,f1,f2)


for k in range(0,N):
    if f1>f2:
        xalt=1*x1; x1=1*x2; f1=1*f2;
        x2 = xust - tau * (xust - xalt); f2=f(x2);
    else:
        xust=1*x2; x2=1*x1; f2=1*f1;
        x1 = xalt + tau * (xust - xalt); f1 = f(x1);
    print(k+1,x1,x2,f1,f2)

x=np.mean([x1,x2]) #birbirine tamamen yaklaşmış olan x1 ve x2 nin son olarak ortalamasını alarak çok düşük hata payıyla sonuç
print(x)


