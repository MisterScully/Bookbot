def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(txt):
    chars = {}
    for c in txt:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars