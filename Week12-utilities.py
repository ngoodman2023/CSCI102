#
#Gage Goodman
#CSCI 102 - Section A
#Week 11 - Part B


def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    return PrintOutput(filename.readlines())

def UpdateString(string, string2, index):
    updated_string = []
    for i in string:
        updated_string.append(i)
    updated_string[index] = string2
    return PrintOutput(''.join(updated_string))

def FindWordCount(user_list, string):
    count = 0
    for i in user_list:
        if(i == string):
            count += 1
    return PrintOutput(count)

def ScoreFinder(user_list, user_floats, player_name):
    upper_names = []
    for i in user_list:
        upper_names.append(i.upper())
    player_name2 = player_name.upper()
    if(player_name2 not in upper_names):
        return PrintOutput('player not found')
    else:
        location = upper_names.index(player_name2)
        output = [str(player_name), 'got a score of', str(user_floats[location])]
        return PrintOutput(' '.join(output))
                           
def Union(list1, list2):
    list3 = []
    for i in list2:
        if i not in list1:
            list3.append(i)
    union_list = list1 + list3
    return PrintOutput(union_list)

def Intersection(list1, list2):
    intersection_list = []
    for i in list1:
        if i in list2:
           intersection_list.append(i)
    return PrintOutput(intersection_list)

def Notln(list1, list2):
    notln_list= []
    for i in list1:
        if i not in list2:
            notln_list.append(i)
    return PrintOutput(notln_list)
    
    
    
            
