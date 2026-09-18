class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        intervals = []
        for i in range(n):
            if first[s[i]] != i:
                continue
            start = i
            end = last[s[i]]
            j = i
            valid = True
            while j <= end:
                c = s[j]
                if first[c] < start:
                    valid = False
                    break
                if last[c] > end:
                    end = last[c]
                j += 1
            if valid:
                intervals.append((start, end))
        
        intervals.sort(key=lambda x: x[1])
        
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
        
        return result