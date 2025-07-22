from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, -1001, 1001)

    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        validLeft = self.valid(node.left, left, node.val)
        validRight = self.valid(node.right, node.val, right)

        return validLeft and validRight
