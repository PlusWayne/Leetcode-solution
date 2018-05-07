# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
            return None
        while head.val==val:
            head=head.next
            try:
                head.val
            except:
                return head
        prev=head
        cur=head.next
        while cur!=None:
            if cur.val==val:
                cur=cur.next
                prev.next=cur
            else:
                prev=cur
                cur=cur.next
        return head
