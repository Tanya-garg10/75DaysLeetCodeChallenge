class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = fast = head
        has_cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        ptr1 = head
        ptr2 = slow 
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1