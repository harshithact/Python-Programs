def solve_sudoku(puzzle):
    def is_valid(puzzle, row, col, val):
        
        # Check row and column
        for i in range(9):
            if puzzle[row][i] == val or puzzle[i][col] == val:
                return False
            
       
    # Check 3x3 square
        
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if puzzle[i][j] == val:
                    return False
        return True

    def backtrack(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for val in range(1, 10):
                        if is_valid(puzzle, i, j, val):
                            puzzle[i][j] = val
                            if backtrack(puzzle):
                                return True
                            puzzle[i][j] = 0
                    return False
        return True

    # Make a copy of the puzzle to avoid modifying the original
    puzzle_copy = [row[:] for row in puzzle]
    # Try to solve the puzzle using backtracking
    if backtrack(puzzle_copy):
        return puzzle_copy
    else:
        return None
