class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)
        c=a+b;
        str_c=bin(c)
        return str_c[2:]