def leap_year(year):
    # If divisible by 400 → leap year
    if year % 400 == 0:
        return True
    # If divisible by 100 (but not 400) → not a leap year
    if year % 100 == 0:
        return False
    # If divisible by 4 (but not 100) → leap year
    if year % 4 == 0:
        return True
    # Otherwise → not a leap year
    return False