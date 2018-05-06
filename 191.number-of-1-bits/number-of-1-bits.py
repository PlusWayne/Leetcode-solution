class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary=bin(n)[2:]
        count=0
        for ele in binary:
            count += int(ele)
        return count
