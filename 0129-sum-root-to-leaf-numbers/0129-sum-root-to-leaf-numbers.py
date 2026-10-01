class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0
            
            current_number = current_number * 10 + node.val
            
            if not node.left and not node.right: 
                return current_number
            
            return dfs(node.left, current_number) + dfs(node.right, current_number)
        
        return dfs(root, 0)