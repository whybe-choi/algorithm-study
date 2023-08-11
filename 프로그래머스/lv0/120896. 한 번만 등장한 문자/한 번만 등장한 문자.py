def solution(s):
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    answer = []
    for k in dic.keys():
        if dic[k] == 1:
            answer.append(k)
    return "".join(sorted(answer))