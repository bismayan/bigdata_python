def number_needed(a, b):
    from collections import Counter
    a_c=Counter(a)
    b_c=Counter(b)
    result=0
    for key in set(a_c.keys()+b_c.keys()):
    	result+=abs(a_c.get(key,0)-b_c.get(key,0))
    return result
    	

#a = raw_input().strip()
#b = raw_input().strip()
a='abc'
b='cde'
print number_needed(a, b)

