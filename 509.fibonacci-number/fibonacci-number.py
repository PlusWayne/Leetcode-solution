class Solution:
    def fib(self, N: 'int') -> 'int':
        if N==0 or N==1:
            return N
        a = 0
        b = 1
        for i in range(2,N+1):
            res = a + b
            b, a = res, b
        return res
