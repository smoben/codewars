def is_isogram(string_):
    string_ = string_.lower()
    array_=[]
    x = len(string_)
    for i in range(x):
        if string_[i] in array_:
            return print(False)
        else:
            array_.append(string_[i])
    return print(True)

is_isogram("benc")

# pythonic solution

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True