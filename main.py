def get_book_content(file_path):
    if file_path == None:
        return
    with open(file_path) as f:
        return f.read()

def number_of_words(book_content):
    word_count = book_content.split()
    print(f"Found {len(word_count)} total words")

def main():
    book_text = get_book_content("books/frankenstein.txt")
    number_of_words(book_text)


main()

