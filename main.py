def read_book():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def count_words(string):
    return len(string.split())


def count_characters(string):
    counts = {}
    for ch in string:
        if not ch.isalpha():
            continue
        lower = ch.lower()
        if lower in counts:
            counts[lower] += 1
        else:
            counts[lower] = 1
    return counts


def vale_dict_orian(d):
    return d["count"]


def book_report(text):
    word_count = count_words(text)
    character_counts = count_characters(text)
    count_dictula = []
    for char in character_counts:
        count_dictula.append({ "char": char, "count": character_counts[char] })
    count_dictula.sort(reverse=True, key=vale_dict_orian)
    output = "--- Begin book report ---\n"
    output += f"\n{word_count} words found in the book."
    for char_dict in count_dictula:
        character = char_dict["char"]
        character_count = char_dict["count"]
        output += f"\nThe {character} character occurs {character_count} times."
    output += "\n--- End book report ---"
    return output


def main():
    text = read_book()
    print(book_report(text)) 


main()
