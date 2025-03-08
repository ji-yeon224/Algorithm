# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 1
    def dfs(self, root: Optional[TreeNode], curDepth: int):
        self.depth = max(self.depth, curDepth)
        if root.left is not None:
            self.dfs(root.left, curDepth+1)
        if root.right is not None:
            self.dfs(root.right, curDepth+1)
        return

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.depth