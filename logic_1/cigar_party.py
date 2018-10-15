def cigar_party(cigars, is_weekend):
  if ((cigars >=40 and cigars <=60 ) or (is_weekend==True and cigars >40 )):
      return True
  elif  cigars >60 and is_weekend==False :
       return False
  elif cigars < 40  : 
   return False
print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
