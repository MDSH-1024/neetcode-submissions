class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val != ".":

                    row_marker = (i, val)
                    column_marker = (val, j)
                    block_marker = (i//3, j//3, val)

                    if row_marker in seen or column_marker in seen or block_marker in seen:
                        return False

                    seen.add(row_marker)
                    seen.add(column_marker)
                    seen.add(block_marker)
        return True