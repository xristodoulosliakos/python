import datetime

def yearCode(year):
    year = year % 100 #take the last two digits
    return ( year + ( year / 4 )) % 7

def monthCode(month):
    if month == 1 :
        return 0
    elif month == 2 :
        return 3
    elif month == 3 :
        return 3
    elif month == 4 :
        return 6
    elif month == 5 :
        return 1
    elif month == 6 :
        return 4
    elif month == 7 :
        return 6
    elif month == 8 :
        return 2
    elif month == 9 :
        return 5
    elif month == 10 :
        return 0
    elif month == 11 :
        return 3
    elif month == 12 :
        return 5

def centuryCode(century):
    century = century / 100 #take the first two digits
    if century == 17 :
        return 4
    elif century == 18 :
        return 2
    elif century == 19 :
        return 0
    elif century == 20 :
        return 6
    elif century == 21 :
        return 4
    elif century == 22 :
        return 2
    elif century == 23 :
        return 0

def leapCode(year, month):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
        if month == 1 or month == 2 :
            return 1
        else:
            return 0
    else:
        return 0

def dayCode(month, year, date):
    year_code = yearCode(year)
    month_code = monthCode(month)
    century_code = centuryCode(year)
    leap_code = leapCode(year, month)
    return (year_code + century_code + month_code + date - leap_code) % 7


def main():
    counter = 0
    now = datetime.datetime.now()
    year = int(now.year)
    month = int(now.month)
    date = int(now.day)
    day = dayCode(month, year, date)

    for currentYear in range(year , year + 10):
        for currentMonth in range (month, 12):
            if day == dayCode(currentMonth,currentYear,date):
                counter += 1
        month = 1

    print "Given the current day,", counter,"days will have the same date as the current day for the next ten years"

if __name__ == "__main__" :
    main()
