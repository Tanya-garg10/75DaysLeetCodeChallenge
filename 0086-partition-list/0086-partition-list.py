class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)

        s = small
        l = large

        while head:
            nxt = head.next
            head.next = None

            if head.val < x:
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next

            head = nxt

        s.next = large.next

        return small.next