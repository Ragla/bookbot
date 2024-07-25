def main():
     book_path = "books/frankenstien.txt"
     text = get_book_text(book_path)
     words = wordcount(text)
     chars_dict = get_char_dict(text)
     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

     print(f"--- Begin report of {book_path} ---")
     print(f"{words} words found in the document")
     print()

     for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

     print("--- End report ---")

def get_book_text(path):
    with open(path) as file:
        return file.read()

def wordcount(text):
    words = len(text.split())
    return(str(words))

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else: 
            chars[lowered] = 1
    return chars

main()