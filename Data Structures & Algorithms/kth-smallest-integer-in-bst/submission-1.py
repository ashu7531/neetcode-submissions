# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        
        def inOrder(node):
            if not node:
                return None
            
            # Traverse left subtree
            inOrder(node.left)
            
            # Increment count and check if it’s the kth element
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse right subtree
            inOrder(node.right)
        
        inOrder(root)
        return self.result

        
    
        
    
        
        
        