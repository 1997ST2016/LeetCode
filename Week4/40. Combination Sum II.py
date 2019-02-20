class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        fl = [0]*len(candidates)
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,fl,0)
        return self.resList
    def dfs(self, candidates, sublist, target, flaglist, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target< candidates[0]:
            return 
        l = None #为了防止重复的比如两个1，那在一层递归只处理一次
        for m in range(len(candidates)):
            n = candidates[m] 
            if n > target:
                return
            if n < last or flaglist[m]==1 or l ==n: 
                #三种情况：1.因为是从小到大，所以n开始要从上一个数以后，
                #2.如果已经使用过，那就继续
                #3.如果在这一层递归的时候 比如有两个1， 那之前做一次1的时候，第二次就不处理了，不然会重复
                continue
            sublist.append(n)
            flaglist[m] = 1 #记录是否 用过的
            self.dfs(candidates,sublist,target - n,flaglist, n)
            flaglist[m] = 0
            l = n
            sublist.pop()
