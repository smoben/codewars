def descending_order(num):
    x = str(num)
    somelist = []
    y = ""
    for i in x:
        z = int(i)
        somelist.append(z)
    somelist.sort(reverse=True)
    for j in somelist:
        k = str(j)
        y = y + k
    return print(int(y))

descending_order(3256)