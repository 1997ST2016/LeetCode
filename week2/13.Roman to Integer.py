class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  
        sum = 0 
        size = len(s)   
        i = 0     
        while i < size:     
            if i > 0 and d[s[i]] > d[s[i-1]]:         
                sum += d[s[i]] -2*d[s[i-1]]   
            else:         
                sum += d[s[i]]         
            i += 1
        return sum
