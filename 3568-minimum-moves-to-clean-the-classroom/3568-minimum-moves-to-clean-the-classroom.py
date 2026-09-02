from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        sr = sc = 0
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = k
                    k += 1

        full = (1 << k) - 1

        best = [[-1] * (1 << k) for _ in range(m * n)]

        start = sr * n + sc
        best[start][0] = energy

        q = deque([(sr, sc, 0, energy)])

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == full:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    pos = nr * n + nc

                    if best[pos][nmask] >= ne:
                        continue

                    best[pos][nmask] = ne
                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1