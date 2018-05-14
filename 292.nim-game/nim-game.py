class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        i) make sure that the number you choose add the number you friend choose equal to four.
        So if n%4!=0, we first choose the number to make sure the number of remain stones have
        n%4=0. Then whatever the number of stone you friend choose, keep doing i). Finally, you friend
        will get four stones, then you win.
        """
        return n%4!=0
