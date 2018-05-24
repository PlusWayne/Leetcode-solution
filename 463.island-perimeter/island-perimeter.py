class Solution:
    def islandPerimeter(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        max_height=len(grid)
        max_width=len(grid[0])
        for i in range(max_height):
            for j in range(max_width):
                 if grid[i][j]==1:
                    res+=self.countStripes(grid,i,j,max_height,max_width)
        return res

    def countStripes(self,grid,i,j,max_height,max_width):
        res=4
        if i-1>=0:
            res-=grid[i-1][j]
        if i+1<=max_height-1:
            res-=grid[i+1][j]
        if j-1>=0:
            res-=grid[i][j-1]
        if j+1<=max_width-1:
            res-=grid[i][j+1]
        return res
