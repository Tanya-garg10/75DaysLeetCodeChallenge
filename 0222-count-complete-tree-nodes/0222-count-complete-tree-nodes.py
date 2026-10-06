class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        left_height = get_left_height(root)
        right_height = get_right_height(root)
        
        if left_height == right_height:
            return (1 << left_height) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)