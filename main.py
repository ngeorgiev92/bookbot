def get_book_text(filedir):
    with open(filedir) as f:
        text = f.read()
    return text

def count_words(filedir):
    with open(filedir) as f:
        text = f.read()
    word_arr = text.split()
    return len(word_arr)

def main():
    print(f"{count_words("books/frankenstein.txt")} words found in the document")

main()
