"""
- DAY 7 -
- Cousins in Binary Tree -

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Ex1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Ex2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Constraints:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None: return False
        parents = {}
        def cousins(node, parent, k):
            if not node or len(parents) == 2:
                return
            else:
                if node.val == x:
                    parents[x] = [parent, k]
                elif node.val == y:
                    parents[y] = [parent, k]
                    
                cousins(node.left, node, k + 1)
                cousins(node.right, node, k + 1)
                
        cousins(root, None, 0)
        return parents[x][0] != parents[y][0] and parents[x][1] == parents[y][1]