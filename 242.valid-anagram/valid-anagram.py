class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp=[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            temp[ord(s[i])-ord('a')]+=1
            temp[ord(t[i])-ord('a')]-=1
        return sum([t==0 for t in temp])==26
        
