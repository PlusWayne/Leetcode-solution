class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1+(num-1)%9 if num!=0 else 0
        # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        
