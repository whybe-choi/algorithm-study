k = int(input())
stack = []

for _ in range(k):
    non_zero = int(input())
    if non_zero:
        stack.append(non_zero)
    else:
        stack.pop()
        
print(sum(stack))