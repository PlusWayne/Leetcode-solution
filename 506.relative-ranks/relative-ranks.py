class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort=sorted(nums,reverse=True)
        rank=["Gold Medal", "Silver Medal", "Bronze Medal"]+ list(map(str,range(4,len(nums)+1)))
        return list(map(dict(zip(sort,rank)).get, nums))
