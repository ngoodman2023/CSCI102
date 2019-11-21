def Intersection(list1, list2):
    intersection_list = []
    for i in list1:
        if i in list2:
           intersection_list.append(i)
    return PrintOutput(intersection_list)
