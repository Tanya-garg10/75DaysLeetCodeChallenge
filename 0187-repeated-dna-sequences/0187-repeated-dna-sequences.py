class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        
        char_to_bits = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        
        encoded = 0
        for i in range(10):
            encoded = (encoded << 2) | char_to_bits[s[i]]
        
        count = defaultdict(int)
        result = []
        count[encoded] = 1
        
        mask = (1 << 20) - 1  

        for i in range(10, n):
            encoded = ((encoded << 2) | char_to_bits[s[i]]) & mask
            count[encoded] += 1
            if count[encoded] == 2:
                result.append(s[i-9:i+1])
        
        return result