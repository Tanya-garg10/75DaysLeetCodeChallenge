class Solution:
    def isSameTree(self, p, q):
        # Case 1: both are null
        if not p and not q:
            return True
        
        # Case 2: one is null
        if not p or not q:
            return False
        
        # Case 3: values differ
        if p.val != q.val:
            return False
        
        # Case 4: check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))