def high_and_low(numbers):
    x = numbers.split()
    a = list(map(int, x))
    numbers = str(max(a)) + " " + str(min(a))
    return numbers

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

# def high_and_low(numbers):
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))

# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"