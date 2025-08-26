# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_most = []

        def bfs(nodes):
            if not nodes: return
            right_most.append(nodes[-1].val)
            children = []
            for node in nodes:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            bfs(children)
        if root: bfs([root])
        return right_most




# Maintain a level
# at each level find the right most node
# stack = []
#          ^
# children = [5, 4] # Each time the last node in the children (if children are inserted into the array correctly) is the right most node

#    1
# 2     3
#   5      4