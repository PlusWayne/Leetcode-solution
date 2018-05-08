class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        if n==0:
            return False
        while n!=1:
            if n%2!=0:
                return False
            else:
                n=n//2
        return True
        """
        # a number is power of two means that only one bit is 1 and others are 0
        if n<=0: return False
        return not n&(n-1)
