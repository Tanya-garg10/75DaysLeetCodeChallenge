class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        
        breakable = [False] * (n + 1)
        breakable[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, min(i + max_len, n) + 1):
                if s[i:j] in word_set and breakable[j]:
                    breakable[i] = True
                    break
        
        if not breakable[0]:
            return []
        
        memo = {}
        
        def dfs(i: int) -> List[str]:
            if i == n:
                return [""]
            if i in memo:
                return memo[i]
            
            sentences = []
            for j in range(i + 1, min(i + max_len, n) + 1):
                word = s[i:j]
                if word in word_set and breakable[j]:
                    for rest in dfs(j):
                        if rest:
                            sentences.append(word + " " + rest)
                        else:
                            sentences.append(word)
            
            memo[i] = sentences
            return sentences
        
        return dfs(0)