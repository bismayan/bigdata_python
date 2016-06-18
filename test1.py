from scipy import *
from pylab import *

color=['r','g','b','k','c','m']

def abc(first,second):
    # type: (int, int)
    """
    plot a stupid curve for two subloops running from 0 to first-1 and 0 to second -1 respectively

    :rtype: none
    """
    for i in range(first):
        for j in range(second):
            x=linspace(20,30,20)
            y=linspace(1,2,20)
            title("Plot "+str(j)+str(i))
            grid()
            plot(y,x,color[i*second+j]+'o-')
            show()

abc(2,3)
