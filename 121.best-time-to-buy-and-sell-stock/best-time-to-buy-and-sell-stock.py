class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MaxCur=0
        MaxPrice=0
        
        for i in range(1,len(prices)):
            MaxCur=max(0, MaxCur+prices[i]-prices[i-1])
            MaxPrice=max(MaxCur,MaxPrice)
        
        return MaxPrice
