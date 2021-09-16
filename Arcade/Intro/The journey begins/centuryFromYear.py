def centuryFromYear(year):
    x = (year//100)
    y = (year % 100)
    if y == 0:
        return (x)
    else:
        return (x+1)