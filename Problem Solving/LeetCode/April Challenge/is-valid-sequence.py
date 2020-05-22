"""
- DAY 30 -
- Check if a String is a Valid Sequence from Root to Leaves Path in BT -

Given a binary tree where each path going from the root to any leaf form a valid sequence, 
check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers a rr and the concatenation 
of all values of the nodes along a path results in a sequence in the given binary tree. 

Ex:
Input: root = [0,1,0,0,1,0,null,nu11,1,0,0], arr = [0,1,0,1] 
Output: true

Constraints: 
• 1 <= arr. length <= 5000 
• 0 <= <= 9 
• Each node's value is between [0 - 9]

Hint 1:
Depth-first search (DFS) with the parameters: current node in the binary tree and current position in the array of integers. 

Hide Hint 2: 
When reaching at final position check if it is a leaf node. 
"""

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root == None or len(arr) == 0: return False
        
        def dfs(self, root, arr, l, pos):
            if root == None:
                return l == 0
            
            if ((root.left == None and root.right == None) and 
                (root.val == arr[pos]) and (pos == len(arr) - 1)):
                return True
            
            return ((pos < l-1) and (root.val == arr[pos]) and 
                    (dfs(self, root.left, arr, l, pos + 1) or 
                     dfs(self, root.right, arr, l, pos + 1)))
            
        pos = 0
        l = len(arr)
        
        return dfs(self, root, arr, l, pos)