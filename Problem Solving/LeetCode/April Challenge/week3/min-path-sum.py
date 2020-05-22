"""
- DAY 18 -
- Minimum Path Sum -

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note:
You can only move either down or right at any point in time.

Ex:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Explanation: 
Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0: return 0
        row, col = len(grid), len(grid[0])
        
        for i in range(0, row):
            for j in range(0, col):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    grid[i][0] += grid[i-1][0]
                elif j > 0:
                    grid[0][j] += grid[0][j-1]
                    
        return grid[-1][-1]