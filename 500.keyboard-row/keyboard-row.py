class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1=set('qwertyuiop')
        row_2=set('asdfghjkl')
        row_3=set('zxcvbnm')
        res=[]
        for word in words:
            if set(word.lower())<=row_1 or\
               set(word.lower())<=row_2 or\
               set(word.lower())<=row_3:
                res.append(word)
        return res
