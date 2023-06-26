import numpy as np #arrayi  numpy arrayi olarak kullanmak daha sağlıklı olur



def f(x1,x2): #fonk
    f=x1**2-x2**2+x1*x2
    return f

def g(x1,x2): #gradyant vektörü    #Yukardiaki fonksiyonun kısmi türeviyle [x1 e göre türev,x2'ye göre türev]
    g=np.array([2*x1+x2,-2*x2+x1])
    return g


#A NOKTASI (X1,X2) f(3,2) --> bu noktadayız.fonksiyon hangi yönde ilerlesin ki azalsın? gradyentin ters yönüne ilerlicez

x1=3
x2=2

x=np.array([x1,x2])

x=x-0.001*g(x1,x2) #ilerleme olayı burda oluyor
print(f(x1,x2))
print(g(x1,x2))
print(x)
#ilerleme miktarımız 10^-3 , gradyantın tersi yönünde ilerliyor.Bu adımlar küçük olmalı yoksa iyi olmaz
# her bi adımda çok az bi küçülme oluyor , fonk yavaş yavaş minimize ediliyor.Gradyantın tersinı kullanarak minimize ediliyor.
# ilerleme adımı çok az olmalı binde bir oranında küçülttük ilerlemeyi
# s yani adım aralığını doğru seçmek çok önemli bunun bulunması da bi boyutlu optimizasyon yöntemlerinden olan golden section ile bulunur.
# optimize edilmiş bi s seçmezsen yanlış sonuçlar doğabiliyor.

x=np.array([x1,x2])
s=0.001 #adım aralığı#adım büyüklüğü -> s yi optimize etmek önemli çok artırınca saçma sonuçlar çıkabiliyor
#adım aralığı s nin aslında golden section ile belirlnemesi gerekir.S nin optimize edilmesi çok önemli
for i in range(0,10):
    p=-g(x[0],x[1])  #p=ilerleme yönü -> gradyentin tersine eşit
    x=x+s*p                        #genel güncelleme kuralı
    print(i,x[0],x[1],f(x[0],x[1]))

#simdi biz minimum noktaya ulaştık mı? Bunun kontrolünü göreceğiz ilerde..