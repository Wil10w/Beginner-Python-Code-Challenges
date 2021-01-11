mystery_value = 0


try:
    outcome = (mystery_value / mystery_value)
    print(outcome)

except:
    try:
        outcome = mystery_value / (mystery_value + 5)
        print(outcome)

    except:
        outcome = mystery_value * 5
        print(outcome)
