class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            if self.prev and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val