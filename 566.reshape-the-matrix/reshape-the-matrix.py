class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) == r*c:
            ret = []
            temp = []
            count = 0
            for row in nums:
                for nm in row:
                    temp.append(nm)
                    count += 1
                    if count == c:
                        ret.append(temp)
                        temp = []
                        count = 0
            return ret
        else:
            return nums
        '''
        if len(nums)*len(nums[0]) != r*c:
            return nums
        list_vector = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                list_vector.append(nums[i][j])
        list_res = []
        for m in range(r):
            list_temp=[]
            for n in range(c):
                list_temp.append(list_vector[m*c+n])
            list_res.append(list_temp)
        return list_res
        '''
