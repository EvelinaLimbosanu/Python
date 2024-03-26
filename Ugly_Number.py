def ugly_number(nr):
    ok = 1
    while ok == 1:
        if nr % 2 == 0:
            nr = nr / 2
        elif nr % 3 == 0:
            nr = nr / 3
        elif nr % 5 == 0:
            nr = nr / 5
        else:
            ok = 0
    if nr != 1:
        return False
    return True


n = 2400

print(ugly_number(n))
