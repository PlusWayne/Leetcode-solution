from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pCounter = Counter(p)
        sCounter = Counter(s[0:len(p)-1])
        res = []
        
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1
            if pCounter == sCounter:
                res.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if  sCounter[s[i-len(p)+1]] == 0:
                sCounter.pop(s[i-len(p)+1])
        return res
                
        
