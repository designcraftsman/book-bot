def get_book_content(file_path):
    if file_path == None:
        return
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_content("books/frankenstein.txt")
    print(book_text)

main()

