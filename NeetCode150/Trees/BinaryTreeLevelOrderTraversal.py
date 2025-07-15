from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [(0, root)]

        while queue:
            h, node = queue.pop(0)
            if h >= len(res):
                res.append([])
            res[h].append(node.val)

            if node.left:
                queue.append((h + 1, node.left))
            if node.right:
                queue.append((h + 1, node.right))

        return res
