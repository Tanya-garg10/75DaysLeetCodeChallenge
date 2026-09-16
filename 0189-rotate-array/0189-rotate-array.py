class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        
        count = 0  
        start = 0
        
        while count < n:
            current = start
            prev = nums[start]
            
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if current == start:
                    break
            
            start += 1