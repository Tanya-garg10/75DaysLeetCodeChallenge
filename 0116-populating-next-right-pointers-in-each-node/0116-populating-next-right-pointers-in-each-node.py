class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node):
            if not node or not node.left:
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return root