class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxCur=0  # record current accumulated value
        maxPrice=0# record total accumulated value
        
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>=0:
                maxCur=maxCur+prices[i]-prices[i-1]
            else:
                maxPrice+=maxCur
                maxCur=0
                
        return maxPrice+maxCur
