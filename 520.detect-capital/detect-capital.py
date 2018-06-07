class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        word = word.replace(' ','')
        word = word[1:]
        if word.islower():
            return True
        return False
