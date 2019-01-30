class Solution:
    def twoSum(self, nums, target):
        dict = {}
        i = 0;
        for i in range(len(nums)):
            if dict.get(target - nums[i],None) == None:
                dict[nums[i]] = i
            else:
                return (dict[target-nums[i]],i)
        i = i+1
