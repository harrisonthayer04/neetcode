# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None
        def dfs(node):
            if not node: 
                return False


            left = dfs(node.left)
            right = dfs(node.right)
            mid = (node is p) or (node is q)

            if (mid + left + right) >= 2:
                self.answer = node
            return mid or left or right

        dfs(root)
        return self.answer

# We want the LOWEST common ancestor
# Start at the bottom nodes, work our way up the tree
# DFS approach