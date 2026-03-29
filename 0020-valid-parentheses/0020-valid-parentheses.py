class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping:  # closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(ch)
        
        return len(stack) == 0