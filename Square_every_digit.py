def square_digits(num):
    x = str(num)
    z = ""
    for i in x:
        y = int(i)**2
        z = z + str(y)
    return print(z)

