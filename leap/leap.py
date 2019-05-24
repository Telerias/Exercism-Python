# PseudoCode
# function is_leap_year(year)
#   if year / 4
#        true - and if year / 100
#            true - then check year / 400
#                if true return true
#                if false return false
#         false - return true
#    if year not / 4 then false


def is_leap_year(year):
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
    
