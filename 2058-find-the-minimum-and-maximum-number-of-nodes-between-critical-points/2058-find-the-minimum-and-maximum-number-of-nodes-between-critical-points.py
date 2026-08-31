class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        first = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr.next:
            is_critical = (
                (curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)
            )

            if is_critical:
                if first == -1:
                    first = index

                if prev_critical != -1:
                    min_dist = min(min_dist, index - prev_critical)

                prev_critical = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]