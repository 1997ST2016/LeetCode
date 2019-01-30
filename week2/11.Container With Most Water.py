class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)   
        maxv = 0 
        j = 0
        k = size - 1
        while j < k:
            if height[j] <= height[k]:
                maxv = max(maxv,height[j] * (k - j))
                j += 1
            else:
                maxv = max(maxv,height[k] * (k - j))
                k -= 1
        return maxv
