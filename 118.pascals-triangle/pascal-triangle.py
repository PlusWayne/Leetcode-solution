class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_res=[[1]]
        if numRows==0:
            return []
        if numRows==1:
            return list_res
        if numRows==2:
            list_res.append([1,1])
            return list_res
        list_res.append([1,1])
        for i in range(2,numRows):
            list_temp=[1]
            for j in range(len(list_res[i-1])-1):
                list_temp.append(list_res[i-1][j]+list_res[i-1][j+1])
            list_temp.append(1)
            list_res.append(list_temp)
        
        return list_res
