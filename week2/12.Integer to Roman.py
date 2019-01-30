class Solution(object):
    def intToRoman(self, nums):
        """
        :type num: int
        :rtype: str
        """
        a = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        b = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        ans = ''
        i = 0
        count = 0
        while nums > 0:
            count = nums/a[i]
            nums %= a[i]
            while count > 0:
                ans += b[i]
                count -= 1
            i += 1
        return ans
