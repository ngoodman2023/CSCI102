def FindWordCount(user_list, string):
    count = 0
    for i in user_list:
        if(i == string):
            count += 1
    return PrintOutput(count)
