from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        def inorderTraversal(root):
            output = []
            def inorderHelper(node):
                if not node:
                    return
                inorderHelper(node.left)
                output.append(node.val)
                inorderHelper(node.right)
            inorderHelper(root)
            return output
    
        tree = inorderTraversal(root)
        return tree[k-1]