class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_sort = sorted(nums)
        return sum(list_sort[::2])
