import pylab as plt


def Listreturn():
    inFile=open("julyTemps.txt",'r')
    lines=inFile.readlines()
    highTemps=[]
    lowTemps=[]
    for line in lines:
        fields=line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            highTemps.append(int(fields[1]))
            lowTemps.append(int(fields[2]))
    return (highTemps,lowTemps)


def producePlot(highTemps,lowTemps):
    """ Produces a plot of the difference between High Temps and Low Temps for all days"""

    diffTemps=[]
    for i in range(len(highTemps)):
        diffTemps.append(highTemps[i]-lowTemps[i])
    plt.plot(range(1,32),diffTemps,'ro-')
    plt.grid()
    plt.xlabel("Days")
    plt.ylabel("Temperature Difference")
    plt.show()

if __name__=="__main__":
    ht,lt=Listreturn()
    producePlot(ht,lt)





