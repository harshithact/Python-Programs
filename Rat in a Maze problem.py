def solve_maze(maze):
    def is_valid(maze, row, col):
        if row < 0 or row >= len(maze) or \
                col < 0 or col >= len(maze[0]) or \
                maze[row][col] == 0:
            return False
        return True

    def backtrack(maze, row, col, path):
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            path.append((row, col))
            return True
        if is_valid(maze, row, col):
            path.append((row, col))
            maze[row][col] = 0
            if backtrack(maze, row + 1, col, path) or \
                    backtrack(maze, row - 1, col, path) or \
                    backtrack(maze, row, col + 1, path) or \
                    backtrack(maze, row, col - 1, path):
                return True
            path.pop()
        return False

    path = []
    backtrack(maze, 0, 0, path)
    return path
