def is_year_leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else: 
        return False
year = int(input("Введите год: "))
is_leap = is_year_leap (year)
print("Год ", year, is_leap)
