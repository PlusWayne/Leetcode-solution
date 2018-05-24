class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag=0
        res=0
        for ele in set(s):
            temp=s.count(ele)
            res+= temp//2*2
            if not flag:
                flag=temp%2
        
        return res+flag
