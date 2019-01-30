# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, s1, s2):
        """
        :type s1: ListNode
        :type s2: ListNode
        :rtype: ListNode
        """
        
        ans = ListNode(0)
        temp = ans
        tempsum = 0
        while True:
            if s1 != None:
                tempsum += s1.val
                s1 = s1.next
            if s2 != None:
                tempsum += s2.val
                s2 = s2.next
            temp.val = tempsum % 10
            tempsum //= 10     #temp除以10的结果向负无穷大取整
            if s1 == None and s2 == None and tempsum == 0:
                break
            temp.next = ListNode(0)
            temp = temp.next
        return ans
