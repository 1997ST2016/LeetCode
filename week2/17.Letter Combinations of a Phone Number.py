class Solution(object):
    def addDigit(self,digit,ans):
        tmp = []
        for element in digit:
            if len(ans) == 0:
                tmp.append(element)
            for s in ans:
                tmp.append(s + element)
        return tmp
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        d = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for element in digits:
            ans = self.addDigit(d[element],ans)
        return ans
