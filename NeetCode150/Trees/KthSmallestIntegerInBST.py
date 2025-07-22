from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cnt = 0
        self.k = 0
        self.res = -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        if root:
            self.res = root.val

        self.search(root)

        return self.res

    def search(self, node: Optional[TreeNode]) -> int:
            if not node:
                return

            self.search(node.left)

            self.cnt += 1
            if self.cnt == self.k:
                self.res = node.val
                return

            self.search(node.right)
