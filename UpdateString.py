def UpdateString(string, string2, index):
    updated_string = []
    for i in string:
        updated_string.append(i)
    updated_string[index] = string2
    return PrintOutput(''.join(updated_string))
