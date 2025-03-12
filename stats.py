def count_words(filedir):
    with open(filedir) as f:
        text = f.read()
    word_arr = text.split()
    return len(word_arr)

def get_book_text(filedir):
    with open(filedir) as f:
        text = f.read()
    return text

def count_by_character(filedir):
    with open(filedir) as f:
        text = f.read()
    characters = list(text)
    characters_dict = {}
    for character in characters :
       lower_case_character = character.lower()
       if not lower_case_character in characters_dict:
           characters_dict[lower_case_character] = 1
       else:
           characters_dict[lower_case_character] += 1
    return characters_dict


