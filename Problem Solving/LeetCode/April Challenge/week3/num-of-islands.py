"""
- DAY 17 -
- Number of Islands -

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Ex1:
Input:
11110
11010
11000
00000

Output: 1

Ex2:
Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        def dfs(grid, i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res