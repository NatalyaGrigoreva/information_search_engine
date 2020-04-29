def compute_lps_array(pat, pat_len, lps):
    len_ = 0
    i = 1
    while i < pat_len:
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i += 1


def knuth_morris_pratt_search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    lps = [0] * pattern_length
    j = 0

    compute_lps_array(pattern, pattern_length, lps)

    i = 0
    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_length:
            print("The search text has index: {}".format(i - j))
            j = lps[j - 1]
        elif i < text_length and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == '__main__':
    input_text = "i'm a text"
    input_pattern = "text"
    knuth_morris_pratt_search(input_pattern, input_text)
