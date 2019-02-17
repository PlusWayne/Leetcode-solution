# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer1 = head
        pointer2 = head
        while pointer1 != None:
            for i in range(n):
                pointer2 = pointer2.next
            if pointer2 ==None:
                head = pointer1.next
                break
            else:
                pointer2 = pointer2.next
            if pointer2 == None:
                pointer1.next = pointer1.next.next
                break
            else:
                pointer1 = pointer1.next
                pointer2 = pointer1
        return head
