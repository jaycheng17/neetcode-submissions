class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for row in range (0,9):
            row_set = set()
            for col in range (0,9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in row_set:
                    return False
                else: 
                    row_set.add(board[row][col])

        # Check Columns
        for col in range(0,9):
            col_set = set()
            for row in range(0,9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in col_set:
                    return False
                else:
                    col_set.add(board[row][col])

        # Check 3 x 3 box
        box_dict = {i: set() for i in range(9)}
        for row in range(0,9):
            for col in range(0,9):
                box_id = (row//3) * 3 + (col//3)
                if board[row][col] == ".":
                    continue
                if board[row][col] in box_dict[box_id]:
                    return False
                else: 
                    box_dict[box_id].add(board[row][col])




        return True