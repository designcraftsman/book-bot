def number_of_words(book_content):
    word_count = book_content.split()
    return len(word_count)

def number_of_characters(book_content):
    character_count = {}
    for i in range(0,len(book_content)):
        if  book_content[i].lower() not in character_count:
            character_count[book_content[i].lower()] = 0
        character_count[book_content[i].lower()] += 1

    return character_count

def sort_on(characters):
    return characters["num"]

def sort_dictionary(characters_dictionary):
    sorted_dictionary = []
    for char in characters_dictionary:
        sorted_dictionary.append({"char":char,"num":characters_dictionary[char]})
    sorted_dictionary.sort(reverse=True,key=sort_on)
    return sorted_dictionary

