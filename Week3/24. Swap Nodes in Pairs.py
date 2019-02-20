# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        ans = ListNode(0)
        ans.next = head 
        temp = ans 
        while temp.next and temp.next.next:
            t = temp.next.next
            temp.next.next = t.next
            t.next = temp.next
            temp.next = t
            temp = temp.next.next 
        return ans.next
    
