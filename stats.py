def count_words(book_string):
    return len(book_string.split())

def count_characters(book_string):
    book = book_string.lower()
    character_dict = {}
    for character in book:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_character_count(character_dict):
    character_count_list = [{"char": x, "count": character_dict[x]} for x in character_dict]
    character_count_list.sort(reverse=True, key=lambda x: x["count"])
    return character_count_list