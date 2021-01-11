# Pessure = (# of moles * gas(0.082057) constant * temperature) / Volume

def find_pressure(moles, temp, vol, R=0.082057):

    pressure = (moles * R * temp) / vol

    return pressure


test_n = 10
test_T = 298
test_V = 5
test_R = 62.364  # Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R=test_R))