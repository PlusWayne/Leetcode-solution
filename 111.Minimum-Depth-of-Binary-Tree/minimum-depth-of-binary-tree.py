# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Three special cases
        # 1) root is null
        # 2) root.left is null
        # 3) root.right is null
        if root==None:
            return 0
        if root.left==None:
            return self.minDepth(root.right)+1
        if root.right==None:
            return self.minDepth(root.left)+1
        
        leftDepth=self.minDepth(root.left)
        rightDepth=self.minDepth(root.right)
        
        if leftDepth>rightDepth:
            return rightDepth+1
        else:
            return leftDepth+1
