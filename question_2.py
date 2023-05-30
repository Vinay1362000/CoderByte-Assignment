def StringChallenge(sen):
    encoded_str = ""
    count = 1
    for i in range(1, len(sen)):
        if sen[i] == sen[i-1]:
            count += 1
        else:
            encoded_str += str(count) + sen[i-1]
            count = 1
    encoded_str += str(count) + sen[-1]
    encoded_str += "16vp578yf"
    encoded_str = ''.join(['X' if (i+1) % 3 == 0 else encoded_str[i] for i in range(len(encoded_str))])
    return encoded_str

print (StringChallenge(input()))
