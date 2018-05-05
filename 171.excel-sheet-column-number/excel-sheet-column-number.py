class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        times=0
        for ele in s[::-1]:
            result += (ord(ele)-ord('A')+1)*(26**times)
            times+=1
        return result
