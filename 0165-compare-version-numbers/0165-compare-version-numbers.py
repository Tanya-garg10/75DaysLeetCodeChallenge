class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')

        for i in range(max(len(a), len(b))):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0
            if x < y:
                return -1
            if x > y:
                return 1

        return 0