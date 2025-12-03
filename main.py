def get_book_text(txt):
    with open(txt) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    words = contents.split()
    num_words = len(words)

    print(f"Found {num_words} total words")

main()