# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:     #if true, we have finished the search for one side return true
            return True
        if p==None or q==None:      #if true, one node is empty and another is not, return false
            return False
        if p.val==q.val:
            x=self.isSameTree(p.left,q.left)  #search left side until reaching the deepest node
            y=self.isSameTree(p.right,q.right)
            return x and y
        else:
            return False
