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

def pretty_print(board: List[List[str]]) -> None:
    for row in board:
        print(*row)
