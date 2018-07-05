class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [[triangle[0][0]]]
        for i in range(1,len(triangle)):
            res_temp = []
            for j in range(len(triangle[i])):
                if j==0:
                    res_temp.append(res[i-1][j]+triangle[i][j])
                if j>0 and j<len(triangle[i])-1:
                    res_temp.append(min(res[i-1][j],res[i-1][j-1])+triangle[i][j])
                if j==len(triangle[i])-1:
                    res_temp.append(res[i-1][j-1]+triangle[i][j])
            res.append(res_temp)
        
        return min(res[-1])
