def solution(s, skip, index):
    alphabet = [i for i in list(map(chr, range(ord('a'), ord('z')+1))) if i not in skip]
    answer = "".join([alphabet[(alphabet.index(j)+index) % len(alphabet)] for j in s])
    return answer