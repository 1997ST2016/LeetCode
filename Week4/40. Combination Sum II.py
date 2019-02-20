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
        l = None #Ϊ�˷�ֹ�ظ��ı�������1������һ��ݹ�ֻ����һ��
        for m in range(len(candidates)):
            n = candidates[m] 
            if n > target:
                return
            if n < last or flaglist[m]==1 or l ==n: 
                #���������1.��Ϊ�Ǵ�С��������n��ʼҪ����һ�����Ժ�
                #2.����Ѿ�ʹ�ù����Ǿͼ���
                #3.�������һ��ݹ��ʱ�� ����������1�� ��֮ǰ��һ��1��ʱ�򣬵ڶ��ξͲ������ˣ���Ȼ���ظ�
                continue
            sublist.append(n)
            flaglist[m] = 1 #��¼�Ƿ� �ù���
            self.dfs(candidates,sublist,target - n,flaglist, n)
            flaglist[m] = 0
            l = n
            sublist.pop()
