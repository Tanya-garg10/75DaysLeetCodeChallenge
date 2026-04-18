class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # If leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse on children
        remaining = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))