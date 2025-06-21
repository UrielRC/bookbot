from stats import count_words, count_characters,sort_book,key_def
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    #frank_book_dir = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_dir = sys.argv[1]
    completed_book = get_book_text(book_dir)
    num_words = count_words(completed_book)
    char_num = count_characters(completed_book)
    sorted_book = sort_book(char_num)
    print (f"============ BOOKBOT ============")
    print (f"Analyzing book found at {book_dir}...")
    print (f"Found {num_words} total words")
    print (f"----------- Character Count ----------")
    for object in range(len(sorted_book)):
        print (f"{sorted_book[object]["char"]}: {sorted_book[object]["num"]}")
    print (f"============= END ===============")
main()