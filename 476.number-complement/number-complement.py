class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 1
        binary=[]
        res=0
        power=0
        while num>0:
            binary.append(1-num%2)
            num //=2
        for ele in binary:
            res+=ele*2**power
            power+=1
        return res
        '''
        i=num.bit_length()
        total=2**i-1
        return num^total
        '''
