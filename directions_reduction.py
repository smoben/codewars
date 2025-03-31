def dir_reduc(arr):
    for i in range(len(arr)):
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH":
            arr.pop(i+1)
        elif arr[i] == "SOUTH" and arr[i+1] == "NORTH":
            arr.pop(i+1)
        elif arr[i] == "EAST" and arr[i+1] == "WEST":
            arr.pop(i+1)
        elif arr[i] == "WEST" and arr[i+1] == "EAST":
            arr.pop(i+1)
        else:
            pass
    return print(arr)

dir_reduc(["SOUTH", "WEST", "NORTH", "SOUTH"])