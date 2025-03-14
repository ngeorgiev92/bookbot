from stats import count_words
from stats import get_book_text
from stats import count_by_character
from stats import make_sorted_list
import sys

def main():
    if not(len(sys.argv)==2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print ("============ BOOKBOT ============")
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        print(f"Analyzing book found at {book_path}")
        print(f"----------- Word Count ----------")
        num_words = count_words(text)
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        chars_dict = count_by_character(text)
        sorted_chars_list = make_sorted_list(chars_dict)
        for char in sorted_chars_list:
            print(f"{char["character"]}: {char["count"]}")
    #chars_dict.sort(reverse=True, key=sort_on)
    #print(chars_dict)
        print("============= END ===============")

main()
