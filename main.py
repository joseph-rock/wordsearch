from typing import List, Dict
import word_dict
import board

def words_in_string(char_list: List[str], indexed_dict: Dict) -> List[str]:
    forward = ''.join(char_list)
    backward = forward[::-1]
    length = len(forward)
    words = []

    for start_index in range(0, length):
        for end_index in range(start_index + 2, length):
            check_forward = forward[start_index: end_index + 1]
            if word_dict.is_word(check_forward, indexed_dict):
                words.append(check_forward)

            check_backward = backward[start_index: end_index + 1]
            if word_dict.is_word(check_backward, indexed_dict):
                words.append(check_backward)

    return words


def main():
    size = 10
    indexed_dict = word_dict.indexed_dict()
    gameboard = board.generate_board(size)

    rows = board.board_rows(gameboard)
    cols = board.board_columns(gameboard)
    diags = board.board_diagonals(gameboard)

    board.pretty_print(gameboard)
    
    words = []
    for row in rows:
        words += words_in_string(row, indexed_dict)
    for col in cols:
        words += words_in_string(col, indexed_dict)
    for diag in diags:
        words += words_in_string(diag, indexed_dict)
    
    words = list(set(words))
    words.sort()

    print()
    print("words:")
    print(*words)


if __name__ == "__main__":
    main()
