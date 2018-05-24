class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[str(i) for i in range(1,n+1)]
        res[2::3]=['Fizz']*len(res[2::3])
        res[4::5]=['Buzz']*len(res[4::5])
        res[14::15]=['FizzBuzz']*len(res[14::15]) 
        return res
