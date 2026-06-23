class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)      
            result.append(node.val) 
            inorder(node.right)    

        inorder(root)
        return result