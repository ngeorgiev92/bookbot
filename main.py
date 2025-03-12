def get_book_text(filedir):
    with open(filedir) as f:
        text = f.read()
    return text

def main():
    print(get_book_text("books/frankenstein.txt"))
main()
