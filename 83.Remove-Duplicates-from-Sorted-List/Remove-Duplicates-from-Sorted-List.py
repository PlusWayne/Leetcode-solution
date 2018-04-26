# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        prev=None
        value=None
        while curr:
            if curr.val==value:   #if equal, begin to delete duplication
                prev.next=curr.next
                curr=curr.next
            else:
                value=curr.val    #if not equal, set the value and move to next
                prev=curr
                curr=curr.next
        return head
