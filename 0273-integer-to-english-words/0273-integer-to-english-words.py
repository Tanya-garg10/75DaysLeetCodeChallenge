class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]
        scales = ["", "Thousand", "Million", "Billion"]

        def three_digits(n):
            parts = []
            if n >= 100:
                parts.append(below_20[n // 100])
                parts.append("Hundred")
                n %= 100
            if n >= 20:
                parts.append(tens[n // 10])
                n %= 10
            if n > 0:
                parts.append(below_20[n])
            return parts

        words = []
        scale_idx = 0
        while num > 0:
            group = num % 1000
            if group > 0:
                chunk = three_digits(group)
                if scales[scale_idx]:
                    chunk.append(scales[scale_idx])
                words = chunk + words
            num //= 1000
            scale_idx += 1

        return " ".join(words)