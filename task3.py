numbers = [1, 2, 2, 3, 3, 4, 5]

def unique_numbers(numbers):
    a = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        a.append(number)

    return a

print(unique_numbers(numbers))