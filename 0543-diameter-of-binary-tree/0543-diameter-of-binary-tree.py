class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            # update diameter
            self.diameter = max(self.diameter, left + right)
            
            # return height
            return 1 + max(left, right)
        
        height(root)
        return self.diameter