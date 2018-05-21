class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp_set=set(t)-set(s)
        if len(temp_set)!=0:
            return list(temp_set)[0]
        else:
            for ele in t:
                if t.count(ele)-s.count(ele)==1:
                    return ele
        
