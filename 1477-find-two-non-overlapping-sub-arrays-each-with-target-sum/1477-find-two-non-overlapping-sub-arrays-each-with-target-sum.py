class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        best = [INF] * (n + 1)  
        ans = INF
        left = 0
        curr_sum = 0
        
        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            best[right + 1] = best[right]  
            
            if curr_sum == target:
                length = right - left + 1
                best[right + 1] = min(best[right], length)
                if best[left] != INF:
                    ans = min(ans, best[left] + length)
        
        return ans if ans != INF else -1