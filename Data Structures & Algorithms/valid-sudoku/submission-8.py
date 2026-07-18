class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #so we can map the indices to the sets containing the nums
        #for rows and cols this is simple its just the num
        #for squares we need some unique index number, could be the sum of r +c //3 ? 
        row_set = [[] for _ in range(9)]
        col_set = [[] for _ in range(9)]
        square_set = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                tile = board[r][c]
                if tile in row_set[r]:
                    return False
                row_set[r].append(tile)
                if tile in col_set[c]:
                    return False
                col_set[c].append(tile)
                idx = (r // 3) * 3 + (c // 3)
                if tile in square_set[idx]:
                    return False
                square_set[idx].append(tile)
        return True