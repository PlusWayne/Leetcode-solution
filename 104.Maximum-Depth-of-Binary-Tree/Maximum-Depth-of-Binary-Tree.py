# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)
        # 先从左边走到树的最下边，然后如果不能走开始走右边
        # 如果一个节点有两个子节点，那么首先会走左边，走到最底厚return回这个节点
        # 之后走右边走到最底，同样return回这个节点，比较那边深度大
        if leftDepth>rightDepth:
            return leftDepth+1
        else:
            return rightDepth+1
