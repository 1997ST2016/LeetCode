class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 
        sum = nums[0]
        d = 0
        for i in range(size):
            if d > 0:
                d += nums[i]
            else:
                d = nums[i]
            if d > sum:
                sum = d
        return sum
