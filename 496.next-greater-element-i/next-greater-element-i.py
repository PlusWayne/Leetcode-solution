class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res=len(findNums)*[-1]
        for i in range(len(findNums)):
            for j in range(nums.index(findNums[i])+1,len(nums)):
                if nums[j]>findNums[i]:
                    res[i]=nums[j]
                    break
        return res
                    
