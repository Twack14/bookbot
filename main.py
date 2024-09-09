def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = count_characters(text)
    #print(f"{word_count} words found in the document")
    #print(chars_dict)
    dict_list = convert_dict(chars_dict)
    dict_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for dict in dict_list:
        if dict["letter"].isalpha():
            print(f"The '{dict['letter']}' character was counted {dict['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    letter_count = {}
    string = text.lower()
    for char in string:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def convert_dict(dict):
    new_list = []
    for key in dict:
        new_dict = {}
        new_dict["letter"] = key
        new_dict["num"] = dict[key]
        new_list.append(new_dict)
    return new_list

def sort_on(dict):
    return dict["num"]

main()
