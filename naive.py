def naive_search(pattern, string):
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length - pattern_length + 1):
        j = 0

        while j < pattern_length:
            if string[i + j] != pattern[j]:
                break
            j += 1

        if j == pattern_length:
            print("The search text has index: {}".format(i))


if __name__ == '__main__':
    input_text = "i'm a text"
    input_pattern = "text"
    naive_search(input_pattern, input_text)
