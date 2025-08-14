from stats import count_words, count_characters, sort_character_count
import sys

def get_book_text(filename):
    print(f"Analyzing book found at {filename}...")
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    book_length = count_words(frankenstein)
    print(f"Found {book_length} total words")

    print("--------- Character Count -------")
    character_count = count_characters(frankenstein)
    sorted_count = sort_character_count(character_count)
    for character in sorted_count:
        if str.isalpha(character["char"]):
            print(f"{character["char"]}: {character["count"]}")

    print("============= END ===============")

main()