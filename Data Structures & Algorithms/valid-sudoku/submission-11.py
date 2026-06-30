from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                value = board[r][c]

                box = (r//3,c//3)

                if (value in rows[r] or value in columns[c] or value in boxes[box]):
                    return False

                rows[r].add(value)
                columns[c].add(value)
                boxes[box].add(value)

        return True