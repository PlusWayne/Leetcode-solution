
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSymmetric2(rootLeft,rootRight):
    if rootLeft==None and rootRight==None:
        return True
    if rootLeft==None or rootRight==None:
        return False
    if rootLeft.val==rootRight.val:
        x=isSymmetric2(rootLeft.left,rootRight.right)
        y=isSymmetric2(rootLeft.right,rootRight.left)
        return x and y
    else:
        return False
class Solution:   
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        if root.left==None or root.right==None:
            return False
        return isSymmetric2(root.left,root.right)
