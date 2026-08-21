class Solution:
    def isNumber(self, s):
        digit = False
        dot = False
        exponent = False
        exponent_digit = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                digit = True
                if exponent:
                    exponent_digit = True

            elif ch in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
                if i == len(s) - 1:
                    return False

            elif ch == '.':
                if dot or exponent:
                    return False
                dot = True

            elif ch in 'eE':
                if exponent or not digit:
                    return False
                exponent = True
                exponent_digit = False

            else:
                return False

        return digit and (not exponent or exponent_digit)