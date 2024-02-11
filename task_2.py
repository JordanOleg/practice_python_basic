def factorial(arg: int) -> int:
    result = 1
    for num in range(1, int(arg) + 1):
        result *= num
    return result


if __name__ == '__main__':
    natural_numbers = list(range(1, 11))
    # 1
    i = 0
    print("foreach in while")
    while i < len(natural_numbers):
        print(natural_numbers[i])
        i += 1
    # 2
    print("foreach in for")
    for item in natural_numbers:
        print(item)
    # 3
    print("Up to what number do you want to make a collection of integers?: ")
    value = input()
    if value.isdigit():
        natural_numbers = list(range(1, int(value) + 1))
        for item in natural_numbers:
            print(item)
    else:
        print("error user collection!")
    # 4
    print("Factorial of which number:")
    value = input()
    if value.isdigit():
        print("Factorial: ", factorial(int(value)))
    # 5
    print("What number to convert to binary form? :")
    value = input()
    if value.isdigit():
        bin_value = bin(int(value))
        print("BIN: ", bin_value)
    else:
        print("error bin numbers!")