def snowed_in(temp, weather, is_celsius=True):
    today_is = True
    if is_celsius is True:
        if temp <= 0:
            if weather == 'sunny':
                today_is = False
        elif temp > 0:
            if weather == "sunny":
                today_is = False
            elif weather == 'snowy':
                today_is = True
            elif weather == 'rainy':
                today_is = False

    else:
        if is_celsius is False:
            if temp <= 32:
                if weather == "sunny":
                    today_is = True
                elif weather == 'snowy':
                    today_is = True
                elif weather == 'rainy':
                    today_is = True
            elif temp > 32:
                if weather == 'sunny':
                    today_is = False
                elif weather == 'snowy':
                    today_is = True
                elif weather == 'rainy':
                    today_is = False
    return today_is


print(snowed_in(0, "sunny"))  # Should print False
print(snowed_in(15, "sunny", is_celsius=False))  # Should print True
print(snowed_in(15, "snowy", is_celsius=False))  # Should print True