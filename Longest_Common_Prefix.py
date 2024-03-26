def prefix(strs):
    ok = 0
    prefix = ""
    index = 0
    while ok == 0 and index < len(strs[0]):
        for element in strs:
            if strs[0][index] == element[index]:
                next_letter = element[index]
            else:
                ok = 1
                next_letter = ""
                break
        prefix = prefix + next_letter
        index += 1
    return prefix


strs = ["flower", "flow", "flight"]
print(prefix(strs))
