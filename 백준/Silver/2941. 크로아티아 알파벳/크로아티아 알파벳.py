alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for alphabet in alphabets:
    if alphabet in string:
        string = string.replace(alphabet, "*")

print(len(string))
        