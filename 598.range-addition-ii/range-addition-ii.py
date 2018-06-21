class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        res_m = m
        res_n = n
        for op in ops:
            res_m = min(res_m,op[0])
            res_n = min(res_n,op[1])
            # print((res_m,res_n))
            
        return res_m*res_n
