from itertools import combinations

a=input()
b=raw_input().split()
c=input()
x=list(combinations(b,c)) 
print float(len([i for i in x if 'a' in i]))/len(x)
