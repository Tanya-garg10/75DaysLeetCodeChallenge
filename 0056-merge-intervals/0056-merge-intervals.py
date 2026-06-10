class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        result = []
        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= current[1]:
                current[1] = max(current[1], interval[1])
            else:
                result.append(current)
                current = interval

        result.append(current)

        return result