from typing import List, Dict
import word_dict
import board


# print(word_dict.is_word('asdfas ec', indexed_dict))
# board.pretty_print(crossword)

def foo(char_list: List[str], indexed_dict: Dict) -> List[str]:
    chars = ''.join(char_list)
    words = []

    for end_index in range(0, len(chars)+1):
        check_str = chars[0: end_index]
        if word_dict.is_word(check_str, indexed_dict):
            words.append(check_str)

    return words


def main():
    indexed_dict = word_dict.indexed_dict()
    crossword = board.generate_board(50)

    word = "cannotasdflkjsdckjvnskjdfkljsdflksjdflksjdflksndclkjsndlkfjslkgjslkdflskdjflskdjcskjldhnfglisjdg".split()

    print(foo(word, indexed_dict))


if __name__ == "__main__":
    main()
