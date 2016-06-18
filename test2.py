from scipy import *
from pylab import *

x=linspace(20,30,500)
figure()
subplot(2,1,1)
plot(x,sin(x),'ro-')
subplot(2,1,2)
plot(x,cos(x),'bo-')
grid()
figure()
plot(x,tan(x),'k-')
grid()
show()
