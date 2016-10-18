class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
	mx=0
	for i in range(len(height)-1):
		for j in range(i+1,len(height)):
			h=min(height[i],height[j])*(j-i)
			if h>mx:
				mx=h
	return mx

print Solution().maxArea([3,2,1,3]) 
