class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_len = 0  
        
        for word in words:
            if line_len + len(line) + len(word) > maxWidth:
                result.append(self._justify(line, line_len, maxWidth))
                line = []
                line_len = 0
            line.append(word)
            line_len += len(word)
       
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
    
    def _justify(self, line, line_len, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - line_len)
        
        total_spaces = maxWidth - line_len
        gaps = len(line) - 1
        base_space, extra = divmod(total_spaces, gaps)
        
        parts = []
        for i, word in enumerate(line[:-1]):
            parts.append(word)
            spaces = base_space + (1 if i < extra else 0)
            parts.append(" " * spaces)
        parts.append(line[-1])
        
        return "".join(parts)