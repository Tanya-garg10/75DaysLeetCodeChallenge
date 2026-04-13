class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        
        # Step 1: Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Step 2: Move both
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Step 3: Delete node
        slow.next = slow.next.next
        
        return dummy.next