class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(nums,sub)
        return self.res

    def dfs(self, Nums, subList):
        if len(subList) == len(Nums):
            #print res,subList
            self.res.append(subList[:])
        for m in Nums:
            if m in subList:
                continue
            subList.append(m)
            self.dfs(Nums,subList)
            subList.remove(m)
