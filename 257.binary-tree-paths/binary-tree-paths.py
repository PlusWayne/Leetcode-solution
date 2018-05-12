# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root!=None:
            res= self.path(root,[],'')
        else:
            res=[]
        return res
    def path(self,root,res,temp):
        if root==None:
            return
        if len(temp)==0:
            temp += str(root.val)
        else:
            temp += ('->'+str(root.val))
        if root.left==None and root.right==None:
            res.append(temp)
            return res
        self.path(root.left,res,temp)
        self.path(root.right,res,temp)
        return res
