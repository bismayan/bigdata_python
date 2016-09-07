from itertools import combinations

def main():
	S=[1,3,4,5,6,-5,4,-2,-6,-8]
        target=48
	val=None
	for i in combinations(S,3):
		su=sum(i)
		if val==None:
			val=su
		elif abs(su-target)<abs(val-target):
			val=su
	print val
	return

if __name__=="__main__":
	main()	
