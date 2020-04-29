def rabin_karp_search(pattern, text, simple_number):
    pattern_length = len(pattern)
    text_length = len(text)
    hash_pattern = 0
    hash_text = 0
    j = 0
    h = 1  # pow(d, M-1)%q

    for i in range(pattern_length - 1):
        h = (h * number_of_characters_in_alphabet) % simple_number

    for i in range(pattern_length):
        hash_pattern = (number_of_characters_in_alphabet * hash_pattern + ord(pattern[i])) % simple_number
        hash_text = (number_of_characters_in_alphabet * hash_text + ord(text[i])) % simple_number

    for i in range(text_length - pattern_length + 1):
        if hash_pattern == hash_text:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            j += 1

            if j == pattern_length:
                print("The search text has index: {}".format(i))

        if i < text_length - pattern_length:
            hash_text = (number_of_characters_in_alphabet * (
                    hash_text - ord(text[i]) * h) + ord(text[i + pattern_length])) % simple_number


if __name__ == '__main__':
    number_of_characters_in_alphabet = 256
    input_text = "i'm a text"
    input_pattern = "text"
    number = 101
    rabin_karp_search(input_pattern, input_text, number)
