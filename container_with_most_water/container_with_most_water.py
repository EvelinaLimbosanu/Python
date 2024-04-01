def most_water(s):
    i = 0
    j = 1
    max_water = -1
    while i < len(s) - 1:
        while j < len(s):
            hight = min(s[i], s[j])
            lenght = j - i
            if hight * lenght > max_water:
                max_water = hight * lenght
            j += 1
        i += 1
        j = i + 1
    return max_water


s = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(most_water(s))
