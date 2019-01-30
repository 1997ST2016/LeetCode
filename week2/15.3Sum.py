class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        while i < size -2:
            tmp = 0 - nums[i]
            j = i + 1
            k = size -1
            while j < k:
                if nums[j] + nums[k] < tmp:
                    j += 1
                elif nums[j] + nums[k] > tmp:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j - 1]:
                            break
                        if nums[k] != nums[k + 1]:
                            break
                        j += 1
                        k -= 1
            i += 1
            while i < size - 2:
                if nums[i] != nums[i - 1]:
                    break
                i += 1
        return ans
