# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        queue=[root]                    # from top to down and left to right, record all nodes level by level.
        size=1                          # each level sizes. root is 1.
        while len(queue)>0:
            temp, count=[], 0           #conut is to record the number of subnodes. temp is to record one level values.
            while size>0:
                node = queue.pop(0)
                temp.append(node.val)
                size -= 1                
                if node.left:
                    queue.append(node.left)
                    count +=1
                if node.right:
                    queue.append(node.right)
                    count +=1
            size=count
            res.append(temp)
        return res[::-1]
