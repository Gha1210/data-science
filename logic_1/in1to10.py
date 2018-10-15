def in1to10(n, outside_mode):
  if n>=1 and n<=10 and outside_mode==False :
  
      return True
  elif n<=1 or n>=10:
    if outside_mode==False:
      return False
    else :
      return True
  elif n>1 and n<10 and outside_mode==True:
    return False