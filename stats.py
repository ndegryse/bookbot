def book_text_to_string(book_text):
    words_in_text = book_text.split()
    num_of_words = len(words_in_text)
    return num_of_words

def counts_char_symb_space(book_text):
    char_to_lower = book_text.lower()
    char = {}
    for character in char_to_lower:
        if character in char:
          char[character] += 1
        else:
          char[character] = 1
    return char

def sorted_list(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
      char_info = {"character": char, "count": count}
      sorted_list.append(char_info)

    def sort_on(dict_item):
        return dict_item["count"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



