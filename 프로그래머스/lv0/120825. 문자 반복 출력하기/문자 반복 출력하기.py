def solution(my_string, n):
    answer = ''.join(string * n for string in my_string)
    return answer