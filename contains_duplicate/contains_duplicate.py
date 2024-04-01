def cotains_duplicate(k, array):
    index = 0
    while index < len(array) - k:
        if array[index] == array[index + k]:
            return True
        index += 1
    return False


array = [1, 2, 3, 1, 2, 3]
k = 2

print(cotains_duplicate(k, array))
