"""
- DAY 20 -
- Kth Smallest Element in a BST -

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Ex1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Ex2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:
* The number of elements of the BST is between 1 to 10^4.
* You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
    
        def inorder(self, node):
            if node == None: return None

            left = inorder(self, node.left)

            if left != None: return left

            self.count += 1
            if self.count == k: return node

            return inorder(self, node.right)
        
        self.count = 0
        return inorder(self, root).val