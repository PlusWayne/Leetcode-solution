# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        list_sum=[]
        self.allPathSum(root,list_sum)
        return True if sum in list_sum else False
        
    def allPathSum(self,root,list_sum,path_sum=0):
        if root==None:
            return 
        path_sum=path_sum+root.val
        if root.left:
            self.allPathSum(root.left,list_sum,path_sum)
        if root.right:
            self.allPathSum(root.right,list_sum,path_sum)
        if root.left is None and root.right is None:
            list_sum.append(path_sum)
