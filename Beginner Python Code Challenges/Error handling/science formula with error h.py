def find_pressure(moles, temp, vol, R=0.082057):
    try:
        pressure = (moles * R * temp) / vol
        return pressure

    except ZeroDivisionError:
        return 'Volume must be greater than 0.'


test_n = 10
test_T = 298
test_V = 3
test_R = 0.082057  # Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R=test_R))