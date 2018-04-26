class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return n
        dp=[]
        dp.append(1)
        dp.append(1)
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
            print(dp[i-1]+dp[i-2])
        return dp[-1]
