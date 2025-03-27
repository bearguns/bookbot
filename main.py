import sys
from stats import count_words, count_characters, make_sorted_list_of_counts


def read_book(path: str):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def book_report(text):
    word_count = count_words(text)
    character_counts = count_characters(text)
    count_dictula = make_sorted_list_of_counts(character_counts)
    output = "--- Begin book report ---\n"
    output += f"\nFound {word_count} total words"
    output += f"\n{character_counts}"
    for char_dict in count_dictula:
        character = char_dict["char"]
        character_count = char_dict["count"]
        output += f"\n{character}: {character_count}"
    output += "\n--- End book report ---"
    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = read_book(path)
        print(book_report(text)) 


main()
