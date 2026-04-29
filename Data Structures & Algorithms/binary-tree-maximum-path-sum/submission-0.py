# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = -1001

        def dfs(node):
            if not node:
                return 0  # contributes nothing

            # Max gain from left and right child (0 means we ignore negative gains)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path that passes through this node (could be the max)
            current = node.val + left_gain + right_gain
            self.best = max(self.best, current)

            # Return max gain from this node to go upward (to be part of a path that extends to parent)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best