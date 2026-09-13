from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        
        if not A or not B:
            return 0
        
        shift_count = defaultdict(int)
        max_overlap = 0
        
        for (ax, ay) in A:
            for (bx, by) in B:
                shift = (bx - ax, by - ay)
                shift_count[shift] += 1
                max_overlap = max(max_overlap, shift_count[shift])
        
        return max_overlap