class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = '+'
        n = len(s)
        
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))
                
                prev_op = char
                num = 0
        
        return sum(stack)