class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = max(freq)

        count_max = freq.count(max_freq)

        ans = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), ans)