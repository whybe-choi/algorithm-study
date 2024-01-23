string = input()
print(1 if ''.join(list(string)[::-1]) == string else 0)