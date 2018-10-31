import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,80)

plt.figure()
plt.plot(x,np.sin(x-3))
plt.plot(-x,np.sin(x-3))

plt.figure()
y=np.sin(x-3)
plt.stem(x,y)
plt.stem(-x,y)

plt.show()






