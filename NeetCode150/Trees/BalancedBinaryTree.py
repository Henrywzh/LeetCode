from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)

        return self.balanced

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l, r = self.height(root.left), self.height(root.right)

        if abs(l - r) > 1:
            self.balanced = False

        return 1 + max(l, r)
