class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        l = len(nums)
        t = 1
        output = []
        for i in range(l):
            output.append(t)
            t *= nums[i]
        
        t = 1
        for i in reversed(range(l)):
            output[i] = output[i] * t
            t *= nums[i]
        return output
