class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #dic = [1,2,3,4,5]
        #dict = ['1','11','21','1211','111221']
        res = ['1']
        for i in range (n):
            num = res [i]
            temp = num [0]
            count = 0
            ans = ''
            for j in range (0,len(num)):
                if num[j] == temp:
                    count += 1
                else:
                    ans += str(count)
                    ans += str(temp)
                    temp = num[j]
                    count = 1
            ans += str(count)
            ans += str(temp)
            res.append(ans)
        return res[n-1]
            
