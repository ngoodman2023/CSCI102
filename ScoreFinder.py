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
