class Solution(object):
    def groupAnagrams(self, strs):
        mp = {}
        
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in mp:
                mp[key] = []
            
            mp[key].append(word)
        
        return mp.values()