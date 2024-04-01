def roman_number(string):
    nr = int(string)
    lst = []
    while nr != 0:
        if nr // 1000:
            multiplu_m = nr // 1000
            lst = lst + ["M"] * multiplu_m
            nr = nr - 1000 * multiplu_m
        elif nr // 900:
            lst = lst + ["CM"]
            nr = nr - 900
        elif nr // 500:
            lst = lst + ["D"]
            nr = nr - 500
        elif nr // 100:
            multiplu_c = nr // 100
            lst = lst + ["C"] * multiplu_c
            nr = nr - 100 * multiplu_c
        elif nr // 90:
            lst = lst + ["XC"]
            nr = nr - 90
        elif nr // 50:
            lst = lst + ["L"]
            nr = nr - 50
        elif nr // 10:
            multiplu_x = nr // 10
            lst = lst + ["X"] * multiplu_x
            nr = nr - 10 * multiplu_x
        elif nr // 9:
            lst = lst + ["IX"]
            nr = nr - 9
        elif nr // 5:
            lst = lst + ["V"]
            nr = nr - 5
        elif nr // 1:
            multiplu_i = nr // 1
            lst = lst + ["I"] * multiplu_i
            nr = nr - 1 * multiplu_i
    return "".join(lst)

