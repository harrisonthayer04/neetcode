# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                current_node = queue.popleft()
                if i is 0:
                    output.append(current_node.val)
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
        return output


# The number of right most nodes is = the height of the tree
# Take the right most at each height
