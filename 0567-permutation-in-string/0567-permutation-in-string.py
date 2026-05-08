class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        
        # frequency of s1
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        
        left = 0
        
        for right in range(len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            
            # keep window size fixed
            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            # compare frequencies
            if need == window:
                return True
        
        return False