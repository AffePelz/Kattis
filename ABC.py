import sys

if __name__ == "__main__":
    first_line = sys.stdin.readline()
    numbers = first_line.split(" ")
    second_line = sys.stdin.readline()
    alphabets = second_line.split("\n")

    int_numbers = []
    for i in numbers:
        int_numbers.append(int(i))

    sorted_numbers = sorted(int_numbers)
    A = sorted_numbers[0]
    B = sorted_numbers[1]
    C = sorted_numbers[2]


    alphabet_value = [A, B, C]
    alphabet = ["A", "B", "C"]

    sorted_alphabets = []
    for i in second_line:
        sorted_alphabets.append(i)

    result = []
    for i in range(0,len(sorted_alphabets) - 1):
        for k in range(0,len(sorted_alphabets) - 1):
            if alphabet[k] == sorted_alphabets[i]:
                result.append(alphabet_value[k])

    print(*result)
