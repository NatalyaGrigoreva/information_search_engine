def bad_char_heuristic(string, size):
    bad_char_ = [-1] * number_of_characters_in_alphabet
    for i in range(size):
        bad_char_[ord(string[i])] = i
    return bad_char_


def boyer_mur_search(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)
    bad_char = bad_char_heuristic(pattern, pattern_length)
    s = 0
    while s <= text_length - pattern_length:
        j = pattern_length - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("The search text has index: {}".format(s))
            s += (pattern_length - bad_char[ord(text[s + pattern_length])] if s + pattern_length < text_length else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])


if __name__ == '__main__':
    number_of_characters_in_alphabet = 256
    input_text = "i'm a text"
    input_pattern = "text"
    boyer_mur_search(input_text, input_pattern)
