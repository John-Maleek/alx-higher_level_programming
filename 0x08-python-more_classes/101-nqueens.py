#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_copy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def get_result(board):
    """Return the list of lists representation of a solved chessboard."""
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                result.append([i, j])
                break
    return (result)


def board_spot(board, row, col):
    """board_spot spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for y in range(col + 1, len(board)):
        board[row][y] = "x"
    # X out all backwards spots
    for y in range(col - 1, -1, -1):
        board[row][y] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    y = col + 1
    for r in range(row + 1, len(board)):
        if y >= len(board):
            break
        board[r][y] = "x"
        y += 1
    # X out all spots diagonally up to the left
    y = col - 1
    for r in range(row - 1, -1, -1):
        if y < 0:
            break
        board[r][c]
        y -= 1
    # X out all spots diagonally up to the right
    y = col + 1
    for r in range(row - 1, -1, -1):
        if y >= len(board):
            break
        board[r][y] = "x"
        y += 1
    # X out all spots diagonally down to the left
    y = col - 1
    for r in range(row + 1, len(board)):
        if y < 0:
            break
        board[r][y] = "x"
        y -= 1


def solve_board(board, row, queens, results):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        results (list): A list of lists of results.
    Returns:
        results
    """
    if queens == len(board):
        results.append(get_result(board))
        return (results)

    for c in range(len(board)):
        if board[row][c] == " ":
            board_duplicate = board_copy(board)
            board_duplicate[row][c] = "Q"
            board_spot(board_duplicate, row, c)
            results = solve_board(board_duplicate, row + 1,
                                        queens + 1, results)

    return (results)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    results = solve_board(board, 0, 0, [])
    for sol in results:
        print(sol)
