class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        result = []
        
        def backtrack(index, current_expr, current_value, last_operand):
            if index == n:
                if current_value == target:
                    result.append(current_expr)
                return
            
            for i in range(index, n):
                operand_str = num[index:i+1]
                
                if len(operand_str) > 1 and operand_str[0] == '0':
                    break
                
                operand = int(operand_str)
                
                if index == 0:
                    backtrack(i + 1, operand_str, operand, operand)
                else:
                    backtrack(i + 1, current_expr + '+' + operand_str, 
                               current_value + operand, operand)
                    backtrack(i + 1, current_expr + '-' + operand_str, 
                               current_value - operand, -operand)
                    backtrack(i + 1, current_expr + '*' + operand_str, 
                               current_value - last_operand + last_operand * operand, 
                               last_operand * operand)
        
        backtrack(0, "", 0, 0)
        return result