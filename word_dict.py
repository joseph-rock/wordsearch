
global KEY_LEN 
KEY_LEN = 3

def indexed_dict() -> dict:
    indexed_dict = {}
    with open('dict.txt', 'r') as f:
        for line in f:
            line = line.strip('\n')
            add_word(line, indexed_dict)
    return indexed_dict

def add_word(word: str, indexed_dict: dict) -> None:
    if len(word) < KEY_LEN:
        return
    
    key = word[0:KEY_LEN]
    if key not in indexed_dict.keys():
        indexed_dict[key] = [word]
    else:
        indexed_dict[key].append(word)

def is_word(word: str, indexed_dict: dict) -> bool:
    if len(word) < KEY_LEN:
        return False
    
    key = word[0:KEY_LEN]
    return key in indexed_dict.keys() and word in indexed_dict[key]
