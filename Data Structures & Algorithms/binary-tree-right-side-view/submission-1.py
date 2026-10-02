# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = Queue()
        queue.put(root)
        res = []
        while not queue.empty():
            q_len = queue.qsize()
            rightside = None
            for i in range(q_len):
                node = queue.get()
                if node:
                    rightside = node
                    queue.put(node.left)
                    queue.put(node.right)
            if rightside:
                res.append(rightside.val)
        return res

            