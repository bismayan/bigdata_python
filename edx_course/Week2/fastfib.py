
memo=[1,0]

def fib(n):
    try:
        return memo[n]
    except IndexError:
        # if n==0:
        #     memo.append(0)
        #     return memo[n]
        # elif n==1:
        #     memo.append(1)
        #     return memo[n]
        #else:
        print "entering recursion"
        memo.append(fib(n-1)+fib(n-2))
        return memo[n]


if __name__=="__main__":
    for i in range(10,0,-1):
        print "Fibonacci number ",i ,"=",fib(i)



