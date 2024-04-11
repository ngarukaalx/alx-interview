#!/usr/bin/python3
"""The N queens puzzle"""
import sys


def fine(row, col, slash, backslash, rowcheck, slashcheck, backslash_check):
    """check if is safe to place a queen"""
    if (slashcheck[slash[row][col]]
            or backslash_check[backslash[row][col]] or rowcheck[row]):
        return False
    return True


def nqueens():
    """initializes the program with param fromstadin"""

    #  if wrong number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # N must be an interger greater or equal 4
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # get the argument from command line
    N = int(sys.argv[1])
    # initializes board with zero
    board = [[0 for i in range(N)]
             for j in range(N)]

    # define helpers
    slash = [[0 for i in range(N)]
             for j in range(N)]

    backslash = [[0 for _ in range(N)] for _ in range(N)]

    # arrays to track rows
    rowcheck = [False] * N

    # track diagonals to check wich is occupied
    d = 2 * N - 1

    slashcheck = [False] * d
    backslash_check = [False] * d
    real_n = N - 1

    # fill helpers
    for row in range(N):
        for col in range(N):
            slash[row][col] = row + col
            backslash[row][col] = row - col + real_n

    all_solutions = []

    def solveNQueens(board, col, slash, backslash, rowcheck,
                     slashcheck, backslash_check):
        """Recusive to find possible solutions"""
        if col == N:
            # add the current solution if all queens are placed
            all_solutions.append([row[:] for row in board])
            return
        for row in range(N):
            if fine(row, col, slash, backslash, rowcheck,
                    slashcheck, backslash_check):
                # place queen and mark position
                board[row][col] = 1
                rowcheck[row] = True
                slashcheck[slash[row][col]] = True

                backslash_check[backslash[row][col]] = True

                solveNQueens(board, col + 1, slash, backslash, rowcheck,
                             slashcheck, backslash_check)

                # backtrack remove queen and reser occupied postion
                board[row][col] = 0
                rowcheck[row] = False
                slashcheck[slash[row][col]] = False
                backslash_check[backslash[row][col]] = False

    solveNQueens(board, 0, slash, backslash, rowcheck,
                 slashcheck, backslash_check)

    for solution in all_solutions:
        queen_postions = []
        for row_index, row in enumerate(solution):
            for col_index, val in enumerate(row):
                if val == 1:
                    queen_postions.append([row_index, col_index])
        print(queen_postions)


if __name__ == "__main__":
    """driver fuction to run the code"""
    nqueens()
