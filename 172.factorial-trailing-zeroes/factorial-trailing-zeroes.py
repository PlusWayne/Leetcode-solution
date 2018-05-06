class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # E.g. 50/5=10 means we have 10's 'five'. However in these 'five', there may exist multiple fives like 25
        # 10/5=2 means there are 2 multiple fives. every 25 (i.e, 5's fives) will bring multiple fives
        count=0
        while n>4:
            count +=n//5
            n=n//5
        return count
