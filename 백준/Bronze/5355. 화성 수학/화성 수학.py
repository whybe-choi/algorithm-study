t = int(input())

for _ in range(t):
    operators = input().split()
    total = float(operators[0])
    for operator in operators[1:]:
        if operator == "@":
            total *= 3
        elif operator == "%":
            total += 5
        else:
            total -= 7
    print(f"{total:.2f}")
         
        