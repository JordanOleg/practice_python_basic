import math


def circle_area(radius: int) -> float:
    return math.pi * radius ** 2


def smallest_number(numbers: list[int]) -> int:
    least = numbers[0]
    for item in numbers[1:]:
        if least > item:
            least = item
    return least


def multiplication_of_all_elements(numbers: list[int]) -> int:
    result = numbers[0]
    for item in numbers[1:]:
        result *= item
    return result


def cubic_row(arg: str) -> int:
    if arg.isdigit():
        result = str()
        for i in range(0, 3):
            result += arg
        return int(result)
    else:
        print("error arg")
        return 0


if __name__ == "__main__":
    # 1
    print("Enter radius: ")
    r = input()
    if r.isdigit():
        print("Area: ", circle_area(int(r)))
    else:
        print("error radius!")
    # 2
    print("""Enter 'n'""")
    n = input()
    print(cubic_row(n))
    # 3
    ints = list(range(1, 21))
    print(sum(ints))
    # 4
    print(multiplication_of_all_elements(ints))
    # 5
    print(smallest_number(ints))
