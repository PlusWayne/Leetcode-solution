# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # use two pointers
        # exploit the same length of intersected list
        #     a_1 a_2 a_3 c_1 c_2
        #         x1        x2
        # b_1 b_2 b_3 b_4 c_1 c_2
        #         x3        x2
        # it must have (x1+x2)+x3=(x3+x2)+x1
        # so we just let one pointer go through the one list and continue to go to other list.
        # we do the same operation to another pointer and they will finally meet in the first intersection node
        if headA==None or headB==None:
            return None
        pA=headA
        pB=headB
        while pA!=pB:
            pA=headB if pA==None else pA.next
            pB=headA if pB==None else pB.next
        return pA
