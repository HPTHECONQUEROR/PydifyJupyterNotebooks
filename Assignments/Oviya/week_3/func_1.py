def numbers(*args):
    total = 0
    for i in args:
        total += i
    return total

print(numbers(1, 2, 3, 4, 5, 6))