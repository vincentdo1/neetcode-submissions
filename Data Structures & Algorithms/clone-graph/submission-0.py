"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if (not node):
            return None
        #cloned_curr = head
        #curr = node
        queue = [node]
        cloned = {}
        #cloned[head] = Node(head.val)
        while (queue):
            curr = queue.pop(0)
            if (curr not in cloned):
                cloned[curr] = Node(curr.val)
            cloned_curr = cloned[curr]

            neighbors = curr.neighbors
            for neighbor in neighbors:
                if (neighbor not in cloned):
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_curr.neighbors.append(cloned[neighbor])
        return cloned[node]
