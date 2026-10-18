class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            row_seen = []
            column_seen = [] 
            for j in range(0,9):
                if board[i][j] != ".":
                    if board[i][j] not in row_seen :
                        row_seen.append(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in column_seen :
                        column_seen.append(board[j][i])
                    else:
                        return False
        
        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                block_seen = []
                for i in range(3):
                    for j in range(3):
                        if board[a + i][b + j] != ".":
                            if board[a + i][b + j] not in block_seen:
                                block_seen.append(board[a + i][b + j])
                            else:
                                return False
        return True