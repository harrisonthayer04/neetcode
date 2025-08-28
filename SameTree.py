# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(q.right, p.right) and self.isSameTree(p.left, q.left)





# decompose each tree into a 
# queue
#           1       < Tree = [1],             Children = [2,3]
#        2      3   < Tree = [1,2,3],         Children = [4,5,6,7]
#      4   5   6  7 < Tree = [1,2,3,4,5,6,7], Children = []

# The number of nodes in tree p = n
# The number of nodes in tree q = m
# Time complexity  O(n+m)
# Space complexity O(n+m)
