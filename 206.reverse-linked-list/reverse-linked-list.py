# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_node=head
        temp=[]
        while temp_node!=None:
            temp.append(temp_node.val)
            temp_node=temp_node.next
        temp_node=head
        for i in temp[::-1]:
            temp_node.val=i
            temp_node=temp_node.next
        
        return head
