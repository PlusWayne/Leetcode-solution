class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_res={}
        length=len(nums)
        if length==1:
            return nums[0]
        for i in nums:
            try:
                dict_res[i]+=1
                if dict_res[i]>length//2:
                    return i
            except:
                dict_res[i]=1
