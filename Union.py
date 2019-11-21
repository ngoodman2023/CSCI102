def Union(list1, list2):
    list3 = []
    for i in list2:
        if i not in list1:
            list3.append(i)
    union_list = list1 + list3
    return PrintOutput(union_list)
