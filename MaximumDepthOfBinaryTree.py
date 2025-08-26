# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.deepest = 0
        def dfs(node, current_depth):
            if not node:
                return
            self.deepest = max(self.deepest, current_depth)
            dfs(node.right, current_depth + 1)
            dfs(node.left, current_depth + 1)
        dfs(root, 1)
        return self.deepest
        

# maintain a deepest height
# DFS
# def dfs(node, current_depth):
#   deepest_height = max(deepest_height, current_depth)
#   base case handling
#   dfs(node.right, current_depth + 1)
#   dfs(node.left, current_depth + 1