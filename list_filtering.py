def filter_list(l):
    somelist = []
    for i in l:
        if isinstance(i, str):
            None
        else:
            somelist.append(i)
    return somelist

filter_list([1, 2, 'a', 'b'])