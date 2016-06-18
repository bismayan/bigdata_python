import scipy as sp
import matplotlib.pylab as plt

x=sp.linspace(10,30,100)
y=sp.cos(x)
plt.plot(x,y,'bo-',x,sp.sin(x),'ro-')
plt.grid()
plt.show()
