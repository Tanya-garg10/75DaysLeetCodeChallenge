from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        count = 0
        
        for num in range(100, 999, 2):  
            need = Counter()
            n = num
            for _ in range(3):
                need[n % 10] += 1
                n //= 10
            
            if all(available[d] >= c for d, c in need.items()):
                count += 1
        
        return count