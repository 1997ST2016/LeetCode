class Solution(object):
    def isPalindrome(self, x):
        strx = str(x) 
      
        r = strx [: : -1] 
        if strx == r:
            return True
        else:
            return False
