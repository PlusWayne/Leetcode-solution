class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        bottom = []
        left = []
        res = 0
        for i in range(len(grid)):
            left.append(max(grid[i]))
            bottom.append(max([tt[i] for tt in grid]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(left[i],bottom[j]) - grid[i][j]
        return res
