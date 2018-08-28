class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        max_Area = 0
        while i<j:
            max_Area = max(max_Area, (j - i)*min(height[i],height[j]))
            if height[i]<height[j]: # if need to move, choose the smaller one to make height taller
                i += 1
            else:
                j -= 1
        return max_Area
            
