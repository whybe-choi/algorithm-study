def solution(numbers):
    string = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(string)):
        if string[i] in numbers:
            numbers = numbers.replace(string[i], str(i)) 
    answer = int(numbers)
    return answer