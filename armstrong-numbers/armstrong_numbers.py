def is_armstrong_number(number):
    length = len(str(number))

    sum = 0
    checknum = number

    while(checknum != 0):
        sum = sum + ((checknum % 10) ** length)
        checknum = checknum // 10
    if sum == number:
        return True
    else:
        return False

