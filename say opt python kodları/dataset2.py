import numpy as np
import math

ti=list(np.arange(-2,2.2,0.2))
yi=[-1.9499,-1.4558,-0.7719,-0.5325,-0.1693,-0.2355,-0.0295,0.1154,-0.0216,0.1753,0.2485,-0.0652,0.2044,
    0.2604,0.0669,0.1113,0.0886,-0.1445,-0.4356,-0.4397,-1.0387]

import matplotlib.pyplot as plt 
plt.scatter(ti, yi, color='darkred')
plt.xlabel('ti')
plt.ylabel('yi')
plt.title('Dataset 1', fontstyle='italic')
plt.grid(color='green',linestyle='--',linewidth=0.1)
plt.show()
