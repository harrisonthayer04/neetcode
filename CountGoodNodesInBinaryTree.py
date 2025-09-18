# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(current_max: int, node: TreeNode) -> None:
            if node.val >= current_max: self.count += 1 
            temp_max = max(current_max, node.val)
            if node.left:  dfs(temp_max, node.left)
            if node.right: dfs(temp_max, node.right)
        dfs(root.val, root)
        return self.count
        
# self.count = 0
# dfs(max_seen, root)
#   if the current node is good:
#       self.count += 1
#   temp_max = max(max_seen, root.val)
#   if right: dfs(temp_max, right)
#   if left: dfs(temp_max, left)