class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target:
                left_index = i
                break
        else:
                return [-1,-1]
            
        for j in range (n-1,-1,-1):
            if nums[j] == target:
                right_index = j
                break        
        return [left_index,right_index]
