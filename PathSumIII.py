# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.pathSums = defaultdict(int)
        self.pathSums[0] = 1
        def dfs(node, current_value):
            if node is None: return
            current_value += node.val
            self.paths += self.pathSums[current_value - targetSum]
            self.pathSums[current_value] += 1
            if node.right:
                dfs(node.right, current_value)
            if node.left:
                dfs(node.left, current_value)
            self.pathSums[current_value] -= 1
        dfs (root, 0)
        return self.paths