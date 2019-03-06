# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        res = []
        self.dfs(root, [], res, sum)
        return res
    
    def dfs(self, root, path, res, sum):
        if root.left == None and root.right== None:
            if sum-root.val == 0:
                res.append(path+[root.val])
            return
        if root.left != None:
            self.dfs(root.left, path+[root.val],res, sum-root.val)
        if root.right != None:
            self.dfs(root.right, path+[root.val],res, sum-root.val)
