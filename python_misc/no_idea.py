from collections import Counter

def get_happy(a,b,c):
    happy=0
    counts=Counter(a)
    inter_b=set(a).intersection(set(b))
    inter_c = set(a).intersection(set(c))
    for el in inter_b:
        happy+=counts[el]
    for el in inter_c:
        happy-=counts[el]
    print happy

if __name__=="__main__":
    inp1=raw_input().split()
    m,n=inp1[0],inp1[1]
    a=tuple(map(int,raw_input().split()))
    b = tuple(map(int, raw_input().split()))
    c= tuple(map(int, raw_input().split()))
    get_happy(a,b,c)