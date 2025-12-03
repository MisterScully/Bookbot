def get_book_text(txt):
    with open(txt) as f:
        file_contents = f.read()
    return file_contents
    
def get_num_words():
    contents = get_book_text("books/frankenstein.txt")
    words = contents.split()
    num_words = len(words)

    print(f"Found {num_words} total words")

get_num_words()