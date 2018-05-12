class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max=0
        Sum=0
        for i in nums:
            if i>=Max:
                Max=i
            Sum+=i
        return Max*(Max+1)//2-Sum if (Max+1)!=len(nums) else Max+1
