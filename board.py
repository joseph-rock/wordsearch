from typing import List
import random

global ALPHABET
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def random_letter() -> str:
    index = random.randint(0, len(ALPHABET) - 1)
    return ALPHABET[index]

def generate_board(dimesion: int) -> List[List[str]]:
    board = []
    for _ in range(dimesion):
        row = []
        for _ in range(dimesion):
            row.append(random_letter())
        board.append(row)
    return board

def board_rows(board: List[List[str]]) -> List[str]:
    rows = []
    for row in board:
        rows.append(''.join(row))
    return rows

def board_columns(board: List[List[str]]) -> List[str]:
    cols = []
    for i in range(len(board[0])):
        col = ''
        for row in board:
            col += row[i]
        cols.append(col)
    return cols

def board_diagonals(board: List[List[str]]) -> List[str]:
    max = len(board)
    diagnals = []

    # L to R top row
    for start in range(max-2):
        diagnal = ''
        x = start
        for row in board:
            if x >= max:
                break
            diagnal += row[x]
            x += 1
        diagnals.append(diagnal)

    # L to R left col
    for y in range(1, max-2):
        diagnal = ''
        for x in range(0, max):
            if y >= max:
                break
            diagnal += board[y][x]
            y += 1
        diagnals.append(diagnal)

    # R to L top row
    for start in range(2, max):
        diagnal = ''
        x = start
        for row in board:
            if x < 0:
                break
            diagnal += row[x]
            x -= 1
        diagnals.append(diagnal)

    # R to L right col
    for y in range(1, max-2):
        diagnal = ''
        for x in range(0, max):
            if y >= max:
                break
            diagnal += board[y][max - x - 1]
            y += 1
        diagnals.append(diagnal)

    return diagnals

def pretty_print(board: List[List[str]]) -> None:
    for row in board:
        print(*row)
