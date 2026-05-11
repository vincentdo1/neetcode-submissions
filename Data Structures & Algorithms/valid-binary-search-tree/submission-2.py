# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, leftValue, rightValue):
            if (root is None):
                return True
            if (not (leftValue < root.val < rightValue)):
                return False
            else:
                return True and valid(root.left, leftValue, root.val) and valid(root.right, root.val, rightValue)
        return valid(root, float("-inf"), float("inf"))