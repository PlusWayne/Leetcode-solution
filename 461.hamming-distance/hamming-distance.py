class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        # to binary
        bin_x=bin(x)[2:]
        bin_y=bin(y)[2:]
        # padding...
        bin_x='0'*(32-len(bin_x))+bin_x
        bin_y='0'*(32-len(bin_y))+bin_y
        # count
        count=0
        for i in range(32):
            if bin_x[i]!=bin_y[i]:
                count+=1
        return count
        """
        return bin(x^y).count('1')
