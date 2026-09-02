class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            kth = prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            curr = prev.next
            prev_node = group_next

            while curr != group_next:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp

            temp = prev.next
            prev.next = kth
            prev = temp