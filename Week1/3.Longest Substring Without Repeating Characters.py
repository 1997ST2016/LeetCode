class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        i = 1
        curbegin = 0
        while i < len(s):
            cur = s.find(s[i],curbegin,i)
            if cur != -1:
                ls = max(ls,i - curbegin)
                curbegin = cur + 1
            i += 1
        if s.find(s[len(s) - 1],curbegin,len(s) - 1) == -1:
            return max(ls,len(s) - curbegin)
        return ls
