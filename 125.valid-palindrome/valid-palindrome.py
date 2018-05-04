class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s=''
        for element in s:
            if element.isalpha() or element.isalnum():
                new_s+=element.lower()
                
        return new_s==new_s[::-1]
