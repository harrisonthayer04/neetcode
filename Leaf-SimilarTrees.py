    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            self.sequence_1 = []
            self.sequence_2 = []

            def dfs(node, sequence):
                if not node:
                    return
                if (node.left is None) and (node.right is None):
                    sequence.append(node.val)
                if node.left and node.right:
                    dfs(node.right, sequence)
                    dfs(node.left, sequence)
                elif node.left:
                    dfs(node.left, sequence)
                elif node.right:
                    dfs(node.right, sequence)

            
            dfs(root1, self.sequence_1)
            dfs(root2, self.sequence_2)

            if len(self.sequence_1) == len(self.sequence_2):
                for index in range(len(self.sequence_1)):
                    if self.sequence_1[index] != self.sequence_2[index]:
                        return False
                return True
            else:
                return False
            

