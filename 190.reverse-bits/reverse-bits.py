class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits=bin(n)[2:]
        bits_padding='0'*(32-len(bits))+bits
        res=int(bits_padding[::-1],2)
        return res
