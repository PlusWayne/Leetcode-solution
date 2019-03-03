class Solution:
    def isValid(self, S: str) -> bool:
        l = len(S)
        while l:
            S = S.replace('abc','')
            new_l = len(S)
            if new_l == l:
                return False
            else:
                l = new_l
        return True
