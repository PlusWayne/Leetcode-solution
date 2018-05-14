class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list_str=str.split(" ")
        if len(list_str)!=len(pattern):
            return False
        return len(set(zip(pattern,list_str)))==len(set(pattern))==len(set(list_str))
