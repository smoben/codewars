def friend(x):
    y = 0
    friends = []
    for name in x:
        y = 0
        for letter in name:
            y = y + 1
        if y == 4:
            friends.append(name)
    return print(friends)

friend(["apa", "anya", "Blanus"])