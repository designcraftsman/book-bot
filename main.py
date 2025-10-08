from stats import number_of_words
from stats import number_of_characters,sort_dictionary
import sys

def get_book_content(file_path):
    if file_path == None:
        return
    with open(file_path) as f:
        return f.read()


def main():
    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_content(sys.argv[1])
    words_count = number_of_words(book_text)
    characters_count = number_of_characters(book_text)
    sorted_characters = sort_dictionary(characters_count)
    print("================BOOKBOT==================\n")
    print("Analyzing your book...\n")
    print("....Word count....\n")
    print(f"Found {words_count} total words")
    print("....Character count....\n")
    print(sorted_characters)


main()

