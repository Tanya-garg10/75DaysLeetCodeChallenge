class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        know_map = {k: v for k, v in knowledge}
        
        output = []
        key_buffer = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
                key_buffer = []
            elif char == ')':
                in_bracket = False
                key = ''.join(key_buffer)
                output.append(know_map.get(key, '?'))
            else:
                if in_bracket:
                    key_buffer.append(char)
                else:
                    output.append(char)
        
        return ''.join(output)