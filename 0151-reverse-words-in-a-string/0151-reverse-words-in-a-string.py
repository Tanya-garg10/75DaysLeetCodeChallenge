class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        reverse(0, n - 1)
        
        write = 0
        read = 0
        while read < n:
            if chars[read] != ' ':
                if write != 0:
                    chars[write] = ' '
                    write += 1
                word_start = write
                while read < n and chars[read] != ' ':
                    chars[write] = chars[read]
                    write += 1
                    read += 1
                reverse(word_start, write - 1)
            else:
                read += 1
        
        return "".join(chars[:write])