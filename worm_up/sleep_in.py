def sleep_in(weekly,vocation) :
    if ((weekly == False) or (vocation == True) ):
        return True 
    else :
        return False

print(sleep_in(False, False))
 
print(sleep_in(True, False)) 
print(sleep_in(False, True))
