class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        dict_temp={}
        for ele in s:
            if dict_temp.__contains__(ele):
                dict_temp[ele]+=1
            else:
                dict_temp[ele]=1
        for i in range(len(s)):
            if dict_temp[s[i]]==1:
                return i
        return -1
        '''
        letter='abcdefghijklmnopqrstuvwxyz'
        count_list=[s.index(l) for l in letter if s.count(l)==1]
        return -1 if len(count_list)==0 else min(count_list)
