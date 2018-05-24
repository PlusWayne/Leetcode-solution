class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1=-0x7fffffff-1  # record the No.1 max number
        max_2=-0x7fffffff-1  # record the No.2 max number
        max_3=-0x7fffffff-1  # record the No.3 max number
        for ele in set(nums):
            if ele>=max_1:
                max_1,max_2,max_3=ele,max_1,max_2
            elif ele>=max_2:
                max_2,max_3=ele,max_2
            elif ele>=max_3:
                max_3=ele
        return  max_3 if len(set(nums))>=3 else max_1
