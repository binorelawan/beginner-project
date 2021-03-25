def is_year_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):

    days = 0
    if is_year_leap(year) == True:
        if month == 2:
            days = 29
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        else:
            days = 31
        print(days)
    else:
        if month == 2:
            days = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        else:
            days = 31
        print(days)
            
if __name__ == "__main__":
    days_in_month(1900, 2)
