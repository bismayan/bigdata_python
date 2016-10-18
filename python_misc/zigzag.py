class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
	s_list=['']*numRows
	len_period=2*numRows-2
	len_s=len(s)
	count=0
	for i in range((len_s/numRows)+1):
		for j in range(numRows):
			if count<len_s:
				s_list[j]+=s[count]
				count=count+1
		for j in range(len_period-numRows):
			if count<len_s:
				s_list[numRows-2-j]+=s[count]
				count=count+1
	print "".join(s_list)
	return

Solution().convert("PAYPALISHIRING", 4)
		

		
