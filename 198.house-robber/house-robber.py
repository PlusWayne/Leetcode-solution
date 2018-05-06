class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        if len(nums)<=1:
            return 0 if len(nums)==0 else nums[0]
        previous_profit_1=nums[0]
        previous_profit_2=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            temp=previous_profit_2
            previous_profit_2=max(previous_profit_1+nums[i],previous_profit_2)
            previous_profit_1=temp
        return previous_profit_2
