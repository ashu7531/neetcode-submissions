/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while (!stack.isEmpty()) {  
            TreeNode node = stack.pop();
            
            if (node != null) {
                int leftHeight = Height(node.left);  
                int rightHeight = Height(node.right); 
                int diff = Math.abs(leftHeight - rightHeight); 
                
                if (diff > 1) { 
                    return false;
                }
                 
                stack.push(node.left);
                stack.push(node.right);
            }
        }
        return true; 
    }
    
    public int Height(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(Height(node.left), Height(node.right));
    }
}