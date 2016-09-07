class LongPalin(object):
	def __init__(self,s=None):
		self.s=s
	
	def set_string(self,s):
		self.s=s
		return 

	def find_palin(self):
		if self.s==None:
			print "String is not Set"
			return
		else:
			long_p=''
			len_long=0
			for i in xrange(len(self.s)-1-len_long):
				for j in xrange(i+1+len_long,len(self.s)+1):
					if self.s[i:j]==self.s[i:j][::-1]:
						long_p=self.s[i:j]
						len_long=len(long_p)
			return long_p

def main():
	obj1=LongPalin(raw_input("Please Input String to test-->"))
	result=obj1.find_palin()
	if result=='':
		print "No Palindromes found"
	else:
		print "Longest palindrome found={}".format(result)
	return 

if __name__=="__main__":
	main()
				
