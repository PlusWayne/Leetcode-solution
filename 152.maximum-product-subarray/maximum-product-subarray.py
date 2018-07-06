class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevPos, prevNeg, res = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            pos = prevPos * nums[i]
            neg = prevNeg * nums[i]
            prevPos = max(nums[i],max(neg,pos))
            prevNeg = min(nums[i],min(neg,pos))
            res = max(res,prevPos)
        
        return res
