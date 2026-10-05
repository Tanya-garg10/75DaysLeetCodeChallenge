class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        bucket_min = [None] * bucket_count
        bucket_max = [None] * bucket_count
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            if bucket_min[idx] is None or num < bucket_min[idx]:
                bucket_min[idx] = num
            if bucket_max[idx] is None or num > bucket_max[idx]:
                bucket_max[idx] = num
        
        max_gap = 0
        prev_max = min_val  
        
        for i in range(bucket_count):
            if bucket_min[i] is None: 
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap