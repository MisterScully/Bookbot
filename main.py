from stats import get_num_words, count_characters


def main():
    book_path = "books/frankenstein.txt"
    txt = get_book_text(book_path)
    num_words = get_num_words(txt)
    chars_dict = count_characters(txt)
    print(f"Found {num_words} total words")
    print(chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
