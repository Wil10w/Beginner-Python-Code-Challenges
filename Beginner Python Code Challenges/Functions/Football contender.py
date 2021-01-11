def is_a_contender(team, wins, losses):
    outcome = ''
    if wins >= 40:
        if losses < 20:
           outcome = 'The ' + team + ' are a contender!'
        else:
            if losses >= 20:
                outcome = 'The ' + team + ' might be a contender!'
    elif wins < 40:
        if losses < 20:
            outcome ='The ' + team + ' might be a contender!'
        else:
            if losses > 20:
                outcome = 'The ' + team + ' are not a contender!'

    return outcome



test_team_name = "Hawks"
test_wins = 10
test_losses = 10

print(is_a_contender(test_team_name, test_wins, test_losses))