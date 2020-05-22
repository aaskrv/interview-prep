"""
- DAY 27 -
- Maximal Square -

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Ex:
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        
        r = len(matrix)
        c = len(matrix[0])
        
        sub = [[int(matrix[l][k]) for k in range(c)] for l in range(r)]
        
        for i in range(1, r): 
            for j in range(1, c): 
                if (int(matrix[i][j]) == 1): 
                    sub[i][j] = min(sub[i][j-1], sub[i-1][j], sub[i-1][j-1]) + 1
                else: 
                    sub[i][j] = 0
        
        l = sub[0][0]
        for i in range(r): 
            for j in range(c): 
                if (l < sub[i][j]): 
                    l = sub[i][j]
        
        return l*l