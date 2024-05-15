def solution(s):
    words = []
    for word in s.split(" "):
        if len(word) > 0:
            if word[0].isalpha():
                word = word[0].upper() + word[1:].lower()
            else:
                word = word[0] + word[1:].lower()
        words.append(word)
    answer = " ".join(words)
    return answer
    