def count_words(text):
    word_arr = text.split()
    return len(word_arr)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_by_character(text):
    characters_dict = {}
    for character in text:
        lower_case_character = character.lower()
        if lower_case_character in characters_dict:
            characters_dict[lower_case_character] += 1
        else:
            characters_dict[lower_case_character] = 1
    return characters_dict

def sort_on(dictionary):
    return dictionary["count"]

def make_sorted_list(dictionary):
    list = []
    for entry in dictionary:
        list.append({"character": entry, "count": dictionary[entry]})
    list.sort(reverse=True, key=sort_on)
    return list



