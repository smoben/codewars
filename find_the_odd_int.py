def find_it(seq):
    seq.sort()
    x = 0
    y = 0
    for i in seq:
        y = y + 1
        if y % 2 == 0:      
            x = x - i
        else:
            x = x + i
    return x

find_it([2, 2, 3, 1, 3])