class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, root.val)

        return self.count

    def traverse(self, node: TreeNode, prevMax: int):
        if node.val >= prevMax:
            self.count += 1
            prevMax = node.val

        if node.left:
            self.traverse(node.left, prevMax)
        if node.right:
            self.traverse(node.right, prevMax)
