# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float(inf)
        self.max_sum_level = 1

        def bfs(nodes, level) -> int:
            if not nodes: return
            sum = 0
            children = []
            for node in nodes:
                sum += node.val
                if node.right: children.append(node.right)
                if node.left:  children.append(node.left)
            if sum > self.max_sum:
                self.max_sum = sum
                self.max_sum_level = level
            bfs(children, level + 1)
        bfs([root], 1)
        return self.max_sum_level

# bfs over the tree
# use a stack to maintain the children nodes of each level
#        1
#      7   0
#    7  -8
#
# self.max_sum = -float(inf)
# self.max_sum_level = 1
# def bfs(nodes:[TreeNode], level):
#   if not nodes: return
#   sum = 0
#   children = []
#   for node in nodes:
#       sum += node.val
#       if node.right: children.append(node.right)
#       if node.left:  children.append(node.left)
#   if sum > self.max_sum:
#       self.max_sum = sum
#       self.max_sum_level = level
#   
#   bfs(children, level + 1)
#   
#   
