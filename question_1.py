def StringChallenge(sen):
    sen = ''.join(c for c in sen if c.isalnum() or c.isspace())
    words = sen.split()
    longest_word = max(words, key=len)
    result = longest_word + "16vp578yf"
    result = ''.join(c if (i + 1) % 3 != 0 else 'X' for i, c in enumerate(result))
    return result

print(StringChallenge(input()))
