class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_temp={}
        s_rep=''
        count=0
        for i in s:
            if i not in s_temp:
               s_temp[i]=count
               s_rep += str(s_temp[i])
               count+=1
            else:
               s_rep += str(s_temp[i])
        t_temp={}
        t_rep=''
        count=0
        for i in t:
            if i not in t_temp:
               t_temp[i]=count
               t_rep += str(t_temp[i])
               count+=1
            else:
               t_rep += str(t_temp[i])
        return s_rep==t_rep
        # one line solution
        # return len(set(zip(t, s))) == len(set(s))==len(set(t))
