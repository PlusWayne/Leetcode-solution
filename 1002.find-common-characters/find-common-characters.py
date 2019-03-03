class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A)==0:
            return []
        if len(A)==1:
            return A[0]
        tt = self.helper(A[0],A[1])
        for i in range(2,len(A)):
            res = self.helper(tt, A[i])
            tt = res
        return list(res)
        
        
    def helper(self, a, b):
        res = ""
        for ele_a in set(a):
            count_a = a.count(ele_a)
            count_b = b.count(ele_a)
            if count_b>0:
                res += min(count_a, count_b)*ele_a
        return res
