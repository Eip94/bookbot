def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    num_words = counter_words(text)
    chars_dict = counter_characters(text)
    filtered_dict = {char: count for char, count in chars_dict.items() if char.isalpha()}
    sorted_list = sorted(filtered_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words was found in this document.")
    for char, letters in sorted_list:
        print(f"The {char} character was found {letters} times.")
    #printdict(chars_dict)
    print("--- End report ---")

def counter_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def counter_characters(text):
    countdict = {}
    ltext = text.lower()
    stext = [char for char in ltext]
    for s in stext:
        if s in countdict:
            countdict[s] += 1
        else:
            countdict[s] = 1
    return countdict

#def printdict(dict):

   # print(dict["num"])
    #print(f"The {l} character was found {n} times."

def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()