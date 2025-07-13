from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        return self.res

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l, r = self.dfs(root.left), self.dfs(root.right)
        self.res = max(self.res, l + r)

        return 1 + max(l, r)
