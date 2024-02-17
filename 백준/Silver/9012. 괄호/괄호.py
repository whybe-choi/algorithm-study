def is_vps(ps):
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack

t = int(input())

for _ in range(t):
    ps = input()
    print("YES" if is_vps(ps) else "NO")