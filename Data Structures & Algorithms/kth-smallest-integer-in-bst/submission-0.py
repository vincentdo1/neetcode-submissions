# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.
class Solution:
    '''
    recursion
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val
        def dfs(node):
            nonlocal count, res
            if (node == None):
                return
            dfs(node.left)
            if (count == 0):
                return
            count -= 1
            if (count == 0):
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
    '''
    # iterative
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while (stack or curr):
            while (curr):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if (k == 0):
                return curr.val
            curr = curr.right
        return root.val
        