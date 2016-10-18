


def running_median(lis):
	curr_lis=[]
	for i in lis:
		curr_lis=insert_el(curr_lis,i)
		print curr_lis
		print "{:.1f}".format((find_med(curr_lis)))
	return


def insert_el(c_list,el):
	pos=find_pos(c_list,el,0,len(c_list)-1)
	return(c_list[:pos]+[el]+c_list[pos:])



def find_pos(l,el,beg,end):
	if l==[]:
		return 0
	if el<=l[beg]:
		return beg
	elif el>=l[end]:
		return end+1
	else:
		mid=(beg+end)/2 
		if el<l[mid]:
			return find_pos(l,el,beg,mid)
		else:
			return find_pos(l,el,mid+1,end)


def find_med(clis):
	l=len(clis)
	if l%2==0:
		return (clis[l/2-1]+clis[l/2])/2.0
	else:
		return float(clis[l/2])



n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
running_median(a)
