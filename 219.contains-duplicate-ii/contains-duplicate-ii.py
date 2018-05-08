class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_store={}
        for i,v in enumerate(nums):
            if v in dict_store and i-dict_store[v]<=k:
                return True
            dict_store[v]=i
        return False
