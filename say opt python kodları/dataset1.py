import numpy as np
import math

ti=[ -2.0, -1.6, -1.2, -0.8, -0.4, 0.0, 0.4, 0.8, 1.2 ,1.6]
yi=[-1.5, 1.30, 2.64, 2.94, 2.62, 2.10, 1.80, 2.15, 3.56, 6.47]

#------------------------------------------------------------------
import matplotlib.pyplot as plt 
plt.scatter(ti, yi, color='darkred')
plt.xlabel('ti')
plt.ylabel('yi')
plt.title('Dataset 1', fontstyle='italic')
plt.grid(color='green',linestyle='--',linewidth=0.1)
plt.show()
#-----------------------------------------------------------------