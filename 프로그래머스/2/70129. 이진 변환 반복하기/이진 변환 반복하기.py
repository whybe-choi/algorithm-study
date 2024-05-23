def solution(x):
    count = 0
    num = 0
    while x != "1":
        count += x.count("0")
        x = x.replace("0", "")
        c = len(x)
        x = bin(c)[2:]
        num += 1
    return [num, count]