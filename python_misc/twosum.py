class Twosum(object):
	def __init__(self,nums=None):
		self.nums=nums
	
	def set_nums(self,nums):
		self.nums=nums
		print "The list of numbers is {}".format(self.nums)
		return
	
	def two_sum(self,target):
		try:
			assert self.nums is not None
		except AssertionError:
			print " Can't check sum as list is not set"
			return None
		for i in xrange(len(self.nums)-1):
			for j in xrange(i+1,len(self.nums)):
				if self.nums[i]+self.nums[j]==target:
					return [i,j]
		return None

	def __del__(self):
		del self.nums
		print id(self)," died"

	
def main():
	obj1=Twosum()
	obj1.set_nums([2,7,7,11,15])
	result=obj1.two_sum(9)
	if result is None:
		print " No Solution found"
	else:
		print "Solution=",result
	return

if __name__=="__main__":
	main()
	
