# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        def dfs(node, left, current):
            if node is None: return
            self.path = max(self.path, current)
            if left: 
                dfs(node.right, False, current + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.right, False, 1)
                dfs(node.left, True, current + 1)
        dfs(root.right, False, 1)
        dfs(root.left, True, 1)

        return self.path





# Trying to find the longest path
# Specifically we want to search in depth of the tree
# dfs

# def longest zig zag:
# output = 0
# def dfs(node, node_direction, count): # Where the direction is the path taken to the node
#   if node_direction == "right":
#       if node.left:
#           count += 1
#           dfs(node.left, left, count)
#   elif node_direction == "left":
#        if node.right:
#           count += 1
#           dfs(node.right, right, count)
# count the root node if 
# right = dfs(root.right, right, 1)
# left = dfs(root.left, left, 1)
# return output