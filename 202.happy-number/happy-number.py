class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_n=[int(ele) for ele in str(n)]
        prev=set([])
        while True:
            temp=0
            for ele in list_n:
                temp+=ele*ele
            if temp==1:
                return True
            list_n=[int(ele) for ele in str(temp)]
            if temp in prev:
                return False
            else:
                prev.add(temp)
