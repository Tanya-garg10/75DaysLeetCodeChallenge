from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []
            
        target = Counter(words)

        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            window = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in target:
                    window.clear()
                    count = 0
                    left = right
                    continue

                window[word] += 1
                count += 1

                while window[word] > target[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return result