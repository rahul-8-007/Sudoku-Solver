def print_board(board):
    """Display the Sudoku board."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        row = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row.append("|")
            row.append(str(board[i][j]) if board[i][j] != 0 else ".")

        print(" ".join(row))


def find_empty(board):
    """Find an empty cell represented by 0."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, row, col):
    """Check whether num can be placed in a cell."""

    # Check the row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """Solve Sudoku using recursive backtracking."""
    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # Backtrack when this choice fails
            board[row][col] = 0

    return False


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_board(board)
    # printing the answer
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists for this puzzle.")


if __name__ == "__main__":
    main()
