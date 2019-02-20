class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 0:
            return 0
 
        internal = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                internal += 1
                length -= 1
            nums[i - internal] = nums[i]
        return length
    
