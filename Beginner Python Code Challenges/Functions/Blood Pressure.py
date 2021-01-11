def check_blood_pressure(sys, dia):
    diagnosis = "none"


    if sys >= 140:
        if dia >= 90:
            diagnosis = 'High'

    elif (sys < 140) and (sys >= 120):
        if (dia < 90) and (dia >= 80):
            diagnosis = 'Pre-high'
        elif dia > 90:
            diagnosis = 'High'
        elif dia < 80:
            diagnosis = 'Pre-high'

    elif (sys < 120) and (sys >= 90):
        if (dia < 80) and (dia >= 60):
            diagnosis = 'Ideal'
        elif dia > 80:
            diagnosis = 'Pre-high'
        elif dia < 60:
                diagnosis = 'Low'

    elif (sys < 90) and (sys >= 70):
        if (dia < 60) and (dia >= 40):
            diagnosis = 'Low'
        elif dia > 60:
                diagnosis = 'Ideal'


    return diagnosis


test_systolic = 88
test_diastolic = 84

print(check_blood_pressure(test_systolic, test_diastolic))
