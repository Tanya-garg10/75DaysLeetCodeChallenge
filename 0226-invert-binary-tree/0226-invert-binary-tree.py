class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # swap children
        root.left, root.right = root.right, root.left
        
        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root