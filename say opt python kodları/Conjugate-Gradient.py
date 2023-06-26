import numpy as np
import math
from ornekFonksiyon1 import f,gradient


def GSf(sk,xk,pk): #goldensection içinde kullanacağımız f anlamında
  
    sonuc=f(xk+sk*pk)
    return sonuc

def GS(xk,pk):
    salt=0
    sust=1
    ds=0.0001
    alpha=(1+math.sqrt(5))/2
    tau=1-1/alpha
    epsilon=ds/(sust-salt)
    N=round(-2.078*math.log(epsilon))  #iterasyon sayısının tamsayı çıkması gerektğinden yuvarlama yaptık
    k=0
    s1=salt+tau*(sust-salt); f1=GSf(s1,xk,pk);
    s2=sust-tau*(sust-salt); f2=GSf(s2,xk,pk);
    
    while abs(s1-s2)>ds:
        k+=1;
        if f1>f2:
            salt=1*s1; s1=1*s2; f1=1*f2;
            s2 = sust - tau * (sust - salt); f2=GSf(s2,xk,pk);
        else:
            sust=1*s2; s2=1*s1; f2=1*f1;
            s1 = salt + tau * (sust - salt); f1 = GSf(s1,xk,pk);
        #print(k+1,s1,s2,f1,f2)
    s=np.mean([s1,s2])  
    return s
#--------------------------------------------------
MaxIter=10000
epsilon1=1e-9 #10^-9-->0.000000001
epsilon2=1e-9
epsilon3=1e-9
#--------------------------------------------------

x1=[0] # fonksiyonun başlangıç noktası(0,0) !!!!!!!!
x2=[0]
xk=np.array([x1[0],x2[0]])
k=0; C1=True; C2=True; C3=True ; C4=True;

prevp=-gradient(xk)
prevg=gradient(xk)


while C1 & C2 & C3 & C4:
    if k==0:
        pk=-gradient(xk)
    else:
        beta=np.dot(gradient(xk), gradient(xk)) /np.dot(prevg,prevg)
        pk=-gradient(xk)+beta*prevp
        prevp=1*pk
        prevg=1*gradient(xk)
    k+=1
    sk=GS(xk, pk)
    #sk=0.2 --> adım aralığını kendin belirlemek istersen üst satırı iptal et bunu aç
    xk=xk+sk*pk
    x1.append(xk[0])
    x2.append(xk[1])
    print('k:',k, ' x1:',format(xk[0],'f') ,' x2: ',format(xk[1],'f'), 'f',format(f(xk),'f'))
    
    C1=k<MaxIter
    C2=epsilon1<abs(f(xk)-f(xk+sk*pk))  
    C3=epsilon2<np.linalg.norm(sk*pk)
    C4=epsilon3<np.linalg.norm(gradient(xk))
 #---------------------------------
C1=k<MaxIter
C2=epsilon1<abs(f(xk)-f(xk+sk*pk))  
C3=epsilon2<np.linalg.norm(sk*pk)
C4=epsilon3<np.linalg.norm(gradient(xk))
#---------------
if not C1:
    print('max iterasyon aşıldı')
if not C2:
    print('fonksiyonun değeri değişmiyor')
if not C3:
    print('ilerleme yönü bulunamıyor')
if not C4:
    print('gradyant sıfıra çok yakın')
    





