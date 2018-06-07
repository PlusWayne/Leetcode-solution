class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        List = s.split(' ')
        for i in range(len(List)):
            List[i] = List[i][::-1]
        return ' '.join(List)
            
