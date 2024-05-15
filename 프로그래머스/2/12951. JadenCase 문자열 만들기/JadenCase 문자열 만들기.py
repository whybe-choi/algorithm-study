def solution(s):
    words = []
    for word in s.split(" "):
        if word:
            if word[0].isalpha():
                word = word[0].upper() + word[1:].lower()
            else:
                word = word[0] + word[1:].lower()
        words.append(word)
    answer = " ".join(words)
    return answer
    