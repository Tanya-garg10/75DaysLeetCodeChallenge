class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # check if start of sequence
            if num - 1 not in num_set:
                length = 1
                
                while num + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest