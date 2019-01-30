import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign = -1
        else:
            sign = 1
        strx = str(abs(x))
        r = strx[::-1] 
        if int(r)>2**31:
            return 0
        else:
            return sign*int(r)
