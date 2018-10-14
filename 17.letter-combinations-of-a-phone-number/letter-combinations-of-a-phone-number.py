class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        PhoneNumber = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z'],
        }
        
        if len(digits)>0:
            out = PhoneNumber[digits[0]]
            
            for i in range(1,len(digits)):
                out = out * len(PhoneNumber[digits[i]])
                out = sorted(out)
                temp = PhoneNumber[digits[i]]
                k = 0
                for j in range(len(out)):
                    out[j] = out[j] + temp[k];
                    if k == len(temp)-1:
                        k = 0
                    else:
                        k += 1
            return out
        else:
            return []
                    
