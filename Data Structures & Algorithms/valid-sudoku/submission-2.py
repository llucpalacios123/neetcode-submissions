class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
   
        seen_y = [set() for _ in range(9)]
        seen_square = [set() for _ in range(9)]

        for i in range(len(board)): 
            seen_x = set()
            for j in range(len(board[i])):

                value = board[i][j]
                if value == '.':
                    continue

                if value in seen_x or value in seen_y[j] or value in seen_square[(i//3*3) + j//3]:
                    return False
                
                seen_x.add(value)
                seen_y[j].add(value)
                seen_square[(i//3*3) + j//3].add(value)

        return True

