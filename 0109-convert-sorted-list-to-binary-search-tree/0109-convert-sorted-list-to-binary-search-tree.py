class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi + 1) // 2  
            root = TreeNode(values[mid])
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root
        
        return build(0, len(values) - 1)