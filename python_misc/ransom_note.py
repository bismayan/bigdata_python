def ransom_note(magazine,ransom):
	for x in ransom:
		 if (x in magazine):
			magazine.remove(x)
		 else:
			return False
	return True


def ransom_note2(magazine,ransom):
	from collections import Counter
	count_ran=Counter(ransom)
	count_mag=Counter(magazine)
	for w,c in count_ran.items():
		print w,c,count_mag.get(w,0),c>count_mag.get(w,0)
		if (c>count_mag.get(w,0)):
			return False
	return True
		 


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note2(magazine, ransom)
if(answer):
    	print "Yes"
else:
        print "No"
