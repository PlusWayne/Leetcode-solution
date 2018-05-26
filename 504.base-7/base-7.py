class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''
        flag=0
        if num==0:
            return '0'
        if num<0:
            num=-num
            flag=1
        while num>0:
            remainder=num%7
            res+=str(remainder)
            num//=7
        return flag*'-'+res[::-1]
