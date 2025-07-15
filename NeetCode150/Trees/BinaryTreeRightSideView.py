from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        d = {}
        queue = [(0, root)]

        while queue:
            h, node = queue.pop(0)
            if h not in d:
                d[h] = []

            d[h].append(node.val)
            if node.left:
                queue.append((h + 1, node.left))
            if node.right:
                queue.append((h + 1, node.right))

        return [d[k][-1] for k in d.keys()]
