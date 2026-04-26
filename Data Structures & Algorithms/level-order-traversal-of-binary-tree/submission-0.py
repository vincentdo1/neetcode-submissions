# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root == None):
            return []
        res = [[root.val]]
        def traverse(height, l, r):
            if (l == None and r == None):
                return
            if (height >= len(res)):
                res.append([])
            if (l != None):
                res[height].append(l.val)
                traverse(height + 1, l.left, l.right)
            if (r != None):
                res[height].append(r.val)
                traverse(height + 1, r.left, r.right)
        traverse(1, root.left, root.right)
        return res

