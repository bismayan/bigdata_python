(X,Y,Z,N)=(int(input("Please input number {}:".format(_+1))) for _ in range(4))


print [[i,j,k] for i in xrange(X+1) for j in xrange(Y+1) for k in xrange(Z+1) if i+j+k!=N]
