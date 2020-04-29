def get_next_state(pat, pat_len, state, x):
    if state < pat_len and x == ord(pat[state]):
        return state + 1
    i = 0
    for ns in range(state, 0, -1):
        if ord(pat[ns - 1]) == x:
            while i < ns - 1:
                if pat[i] != pat[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0


def finite_automata(pat, pat_len):
    fa = [[0 for _ in range(number_of_characters_in_alphabet)] for _ in range(pat_len + 1)]
    for state in range(pat_len + 1):
        for x in range(number_of_characters_in_alphabet):
            z = get_next_state(pat, pat_len, state, x)
            fa[state][x] = z
    return fa


def finite_automata_search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    finite_auto = finite_automata(pattern, pattern_length)
    state = 0
    for i in range(text_length):
        state = finite_auto[state][ord(text[i])]
        if state == pattern_length:
            print("The search text has index: {}".format(i - pattern_length + 1))


if __name__ == '__main__':
    number_of_characters_in_alphabet = 256
    input_text = "i'm a text"
    input_pattern = "text"
    finite_automata_search(input_pattern, input_text)
