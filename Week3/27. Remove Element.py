class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0;j = 0
        size = len(nums)
        for j in range (0,size):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1;j += 1
        return i
                    
