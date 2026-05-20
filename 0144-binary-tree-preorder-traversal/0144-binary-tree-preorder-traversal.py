class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            result.append(node.val)   
            dfs(node.left)            
            dfs(node.right)           
        
        dfs(root)
        return result