# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        depth = 1
        queue = deque([(root, depth)])
        rightSideNums = [root.val]
        while queue:
            cur, curDepth = queue.popleft()
            if cur.right is not None:
                if len(rightSideNums) == curDepth:
                    rightSideNums.append(cur.right.val) 
                queue.append((cur.right, curDepth+1))
            if cur.left is not None:
                if len(rightSideNums) == curDepth:
                    rightSideNums.append(cur.left.val)
                queue.append((cur.left, curDepth+1)) 
        return rightSideNums


        