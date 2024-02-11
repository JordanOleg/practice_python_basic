
if __name__ == '__main__':
    print("Enter a number: ")
    value = input()
    if value.isdigit():
        number = int(value)
        print(number % 3 == 0)
    else:
        print("The argument is not a number")
