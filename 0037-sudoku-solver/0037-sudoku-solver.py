class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    b = (r // 3) * 3 + c // 3
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        b = (r // 3) * 3 + c // 3

                        for num in "123456789":
                            if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[b].add(num)

                                if backtrack():
                                    return True

                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[b].remove(num)

                        return False

            return True

        backtrack()
        