from itertools import product

def get_max(K,M,data):
    prod_array=[i for i in product(set(data[0]),set(data[1]))]
    for i in range(2,K):
        prod_new=[]
        for j in product(prod_array,set(data[i])):
            a=list(j[0])
            a.append(j[1])
            prod_new.append(a)
        prod_array=prod_new
    print max([sum([j*j for j in i])%M for i in prod_array])
    return

def get_max2(K,M,data):
    print max([sum(map(lambda i:i**2,prod))%M for prod in product(*data)])
    return


if __name__=="__main__":
    #inp1 = raw_input().split()
    #K,M = int(inp1[0]), int(inp1[1])
    #data=[]
    # for i in xrange(K):
    #     data.append(tuple(map(int,raw_input().split())[1:]))
    # print data
    # data.append((0,))
    # print data
    # get_max(K,M,data)
    get_max2(3,12,[[1,2,3],[4,5,6],[0,]])