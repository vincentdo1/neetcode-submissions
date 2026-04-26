# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        curr = root
        if (p.val >= q.val):
            tmp = q
            q = p
            p = tmp
        while (curr != None):
            if (curr.val >= p.val and curr.val <= q.val):
                res = curr
                return res
            elif (curr.val > q.val):
                curr = curr.left
            elif (curr.val < p.val):
                curr = curr.right
        return res