class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        
        def solve(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]
            
            if expr.isdigit():
                return [int(expr)]
            
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i+1:])
                    
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            
            memo[expr] = results
            return results
        
        return solve(expression)