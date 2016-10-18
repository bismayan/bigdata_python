def array_left_rotation(a, n, k):
	b=[0]*n
	for i in range(n):
		b[(i-k)%n]=a[i]
	return b	

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
