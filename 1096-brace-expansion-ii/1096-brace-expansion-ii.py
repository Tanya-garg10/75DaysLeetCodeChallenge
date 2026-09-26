class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.expr = expression
        self.pos = 0
        result_set = self.parse_union()
        return sorted(result_set)
    
    def parse_union(self) -> set:
        result = self.parse_concat()
        while self.pos < len(self.expr) and self.expr[self.pos] == ',':
            self.pos += 1  
            result |= self.parse_concat()
        return result
    
    def parse_concat(self) -> set:
        result = {""}
        while self.pos < len(self.expr) and self.expr[self.pos] not in ',}':
            factor_set = self.parse_factor()
            result = {a + b for a in result for b in factor_set}
        return result
    
    def parse_factor(self) -> set:
        if self.expr[self.pos] == '{':
            self.pos += 1  
            inner = self.parse_union()
            self.pos += 1  
            return inner
        else:
            letter = self.expr[self.pos]
            self.pos += 1
            return {letter}     