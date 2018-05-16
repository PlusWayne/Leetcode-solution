class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=list('aeiouAEIOU')
        s=list(s)
        point1=0
        point2=len(s)-1
        while point1<point2:
            if s[point1] in vowels and s[point2] in vowels:
                s[point1],s[point2]=s[point2], s[point1]
                point1 +=1
                point2 -=1
            elif s[point1] in vowels:
                point2 -=1
            elif s[point2] in vowels:
                point1 +=1
            else:
                point1 +=1
                point2 -=1
        return ''.join(s)
