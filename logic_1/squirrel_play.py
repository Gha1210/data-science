def squirrel_play(temp, is_summer):
  if temp>=0:
    
    if temp >=60 and temp <=90 and is_summer==False:
      return True
    elif temp>=60 and temp<=100 and is_summer==True:
      return True
  
    return False
  return False
