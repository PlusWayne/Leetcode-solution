class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capital=[chr(i) for i in range(ord('A'),ord('Z')+1)]
        result=''
        while n>0:
            result+=capital[(n-1)%26]
            n=(n-1)//26
        return result[::-1]
