class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        
        if is_valid(s):
            return [s]
        
        visited = {s}
        current_level = {s}
        
        while current_level:
            next_level = set()
            
            for string in current_level:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue  
                    candidate = string[:i] + string[i+1:]
                    if candidate not in visited:
                        visited.add(candidate)
                        next_level.add(candidate)
            
            valid_results = [string for string in next_level if is_valid(string)]
            if valid_results:
                return valid_results
            
            current_level = next_level
        
        return [""]  