
def validare(my_str):
    lst = list(my_str)
    if len(lst) % 2 != 0:
        return False
    index = 0
    while index < len(lst):
        if (
            (lst[index] == ")" and lst[index - 1] == "(")
            or (lst[index] == "}" and lst[index - 1] == "{")
            or (lst[index] == "]" and lst[index - 1] == "[")
        ):
            del lst[index]
            del lst[index - 1]
            index = index - 2
        index = index + 1
    if len(lst) != 0:
        return False
    else:
        return True


example = "{[]}(){()}"
print(validare(example))
