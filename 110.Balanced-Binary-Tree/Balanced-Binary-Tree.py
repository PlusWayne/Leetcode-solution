# This is not the best solution and compute depth too many times
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        if root == None:
            return True
        if self.jugle(root):
            x = self.isBalanced(root.left)
            y = self.isBalanced(root.right)
            return x and y
        else:
            return False

    def jugle(self, root):
        if root==None:
            return True
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(right - left) > 1:
            return False
        else:
            return True

    def maxDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth < rightDepth:
            return rightDepth + 1
        else:
            return leftDepth + 1
