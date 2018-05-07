class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 0
        Bool_list=[True]*n
        Bool_list[0],Bool_list[1]= False, False
        for i in range(2,int(n**0.5)+1):
            if Bool_list[i]:
               Bool_list[i*i:n:i]=[False]*len(Bool_list[i*i:n:i]) #from i*i to the end with step i. (i*i,i*(i+1)...)
        return sum(Bool_list)
