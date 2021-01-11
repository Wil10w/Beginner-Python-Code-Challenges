from datetime import date

def get_todays_date():
    d = date.today()
    f_mat = d.strftime("%Y/%m/%d")

    return f_mat


print(get_todays_date())