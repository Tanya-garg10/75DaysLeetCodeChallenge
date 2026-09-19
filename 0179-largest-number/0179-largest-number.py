from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1   
            else:
                return 0
        
        strs.sort(key=cmp_to_key(compare))
        
        result = "".join(strs)
     
        if result[0] == '0':
            return "0"
        
        return result