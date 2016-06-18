import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    nsuc=0.0
    for i in range(numTrials):
        print "New Trial no-",i+1
        balls=['r','b','r','b','r','b']
        nb=0
        nr=0
        for j in range(3):
            index=random.randint(0,len(balls)-1)
            print "ball of color ",balls[index], " picked"
            if(balls[index]=='r'):
                nr=nr+1
            else:
                nb=nb+1
            if (nb*nr !=0):
                print "Trial Failed"
                break
            del balls[index]
            print "new list=",balls
        print "Trial Done"," nb=",nb,"nr=",nr
        if (nb==3 or nr==3):
            print "Success"
            nsuc=nsuc+1.0
            print "New nsuc=",nsuc
    print "nsuc=",nsuc
    return(nsuc/numTrials)


print(noReplacementSimulation(1000))