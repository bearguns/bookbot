def count_words(string: str):
    return len(string.split())


def count_characters(string: str):
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


def sort_on(d: dict):
    return d["count"]


def make_sorted_list_of_counts(character_counts):
    out = []
    for char in character_counts:
        out.append({ "char": char, "count": character_counts[char] })
    out.sort(reverse=True, key=sort_on)
    return out
