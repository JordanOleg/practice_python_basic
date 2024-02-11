
def delete_duplicate(numbers: list[int]) -> list[int]:
    dep = []
    i = 0
    while i < len(numbers):
        if numbers[i] in dep:
            del numbers[i]
        else:
            dep.append(numbers[i])
            i += 1
    return numbers
if __name__ == "__main__":
    naturals_numbers =  [1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 7]
    print("origin: ", naturals_numbers)
    print("result: ", delete_duplicate(naturals_numbers))