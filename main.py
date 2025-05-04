import sys
from stats import (
    number_of_words as get_num_words,
    count_letters as get_chars_dict,
    sort_chars as chars_dict_to_sorted_list,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    # Get the text from the book
    text = get_book_text(book_path)
    
    # Print the length of the text
    print(f"Length of text: {len(text)}")

    e_t_counts = count_specific_letters(text)
    print(f"Direct count e: {e_t_counts['e']}")
    print(f"Direct count t: {e_t_counts['t']}")
    print("First 100 characters:", text[:100])

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

    chars_dict = get_chars_dict(text)
    print(f"e: {chars_dict.get('e', 0)}")
    print(f"t: {chars_dict.get('t', 0)}")


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def count_specific_letters(text, letters=['e', 't']):
    text = text.lower()
    counts = {letter: text.count(letter) for letter in letters}
    return counts



def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
