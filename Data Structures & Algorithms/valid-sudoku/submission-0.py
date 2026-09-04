class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #cols
        cols = defaultdict(set)
        #rows
        rows = defaultdict(set)
        # 3x3 grid
        squares = defaultdict(set)
        # (r//3 * 3) + c//3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in rows[(r//3, c//3)]):
                   return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                rows[(r//3, c//3)].add(board[r][c])
        return True
                
