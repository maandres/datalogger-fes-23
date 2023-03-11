#import pandas as pd

#print(pd._version_)

import matplotlib.pyplot as plt
import numpy as np
import time

f= 10
T = 1/f

t=np.linspace(0,5*T, 5*100)

s1= 1*np.sin(2*np.pi*f+t)

fig, ax= plt.subplots()
ax.plot(t,s1,t)
plt.show()

#https://www.youtube.com/watch?v=KJwQzJ6SUU4
#Video utilitzat
