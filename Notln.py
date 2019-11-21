def Notln(list1, list2):
    notln_list= []
    for i in list1:
        if i not in list2:
            notln_list.append(i)
    return PrintOutput(notln_list)
