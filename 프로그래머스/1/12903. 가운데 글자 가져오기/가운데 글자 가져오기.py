def solution(s):
    answer = s[len(s)//2] if len(s) % 2 == 1 else s[len(s)//2 - 1:len(s)//2 + 1]
    return answer