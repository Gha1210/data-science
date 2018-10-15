def count_code(str):
  c=0
  if len(str)>=4:
    
    for i in range(len(str)):
      if str[i]=="c" :
        if i+1<len(str):
          
          if str[i+1]=="o":
            if i+3<len(str):
              if str[i+3]=="e":
                c=c+1
      
  return c