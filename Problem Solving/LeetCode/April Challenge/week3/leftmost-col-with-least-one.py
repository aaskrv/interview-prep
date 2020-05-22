"""
- DAY 21 -
- Construct Binary Search Tree from Preorder Traversal -

(This problem is an interactive problem.) 

A binary matrix means that all elements are 0 or 1 . For each individual row of the matrix, this row is sorted in non-decreasing order. 

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return —1 . 

You can't access the Binary Matrix directly. You may only access the matrix using a Bina ryMat rix interface: 
• BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col.) (0-indexed). 
• BinaryMatrix. dimensions ( ) returns a list of 2 elements [ rows, cols] , which means the matrix is rows * cols 

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt 
to circumvent the judge will result in disqualification. 

For custom testing purposes you're given the binary matrix mat as input in the following four examples. 
You will not have access the binary matrix directly. 

Ex1:
Input: mat = [[0, 0], [1, 1]]
Output: 0
"""

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        
        n, m = dim[0], dim[1]
        
        leftmost = []
        
        for i in range(0, n):
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r)//2
                
                x = binaryMatrix.get(i, mid)
                
                if (x == 1 and (mid == 0 or binaryMatrix.get(i, mid-1) == 0)):
                    leftmost.append(mid)
                    break
                elif x == 0:
                    l = mid + 1
                else:
                    r = mid - 1
        
        if not leftmost: return -1
        else: return min(leftmost)