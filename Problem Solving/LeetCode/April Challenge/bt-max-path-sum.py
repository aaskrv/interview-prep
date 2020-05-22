"""
- DAY 29 -
- Binary Tree Maximum Path Sum -

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child 
connections. The path must contain at least one node and does not need to go through the root.

Ex1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Ex2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPath(self, root):
            if root == None: return 0
        
            left = maxPath(self, root.left)
            right = maxPath(self, root.right)

            single = max(max(left, right) + root.val, root.val)

            top = max(single, left + right + root.val)

            maxPath.res = max(maxPath.res, top)

            return single
        
        maxPath.res = -sys.maxsize
        
        maxPath(self, root)
        
        return maxPath.res