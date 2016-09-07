from itertools import combinations

def main():
	S=[1,3,4,5,6,-5,4,-2,-6,-8]
	return {tuple(sorted(i)) for i in combinations(S,3) if sum(i)==0}
	

if __name__=="__main__":
	 res=main()
	 for i in res:
		print i
	
