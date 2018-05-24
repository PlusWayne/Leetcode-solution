class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        res=''
        temp=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if num<0:
            num=2**32+num
        while num>0:
            mod_num=num%16
            res+=temp[mod_num]
            num=num//16
        return res[::-1]
