# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        queue = deque([(root, root.val)])

        while len(queue) > 0:
            for i in range(len(queue)):
                current, current_sum = queue.popleft()
                if not current.left and not current.right and (current_sum == targetSum):
                    return True
                if current.left:
                    queue.append([current.left, current_sum + current.left.val])
                if current.right:
                    queue.append([current.right, current_sum + current.right.val])
        return False