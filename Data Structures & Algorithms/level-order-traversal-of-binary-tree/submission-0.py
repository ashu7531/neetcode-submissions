# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = Queue()
        level = 0
        queue.put((root, level))
        res = []
        while (not queue.empty()):
            node, level = queue.get()
            if node:
                if len(res) == level:
                    res.append([node.val])
                else:
                    res[level].append(node.val)
                queue.put((node.left, level+1))
                queue.put((node.right, level+1))
        return res
