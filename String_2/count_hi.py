def count_hi(str):
  c=0
  x=len(str)
  for i in range(x-1):
    if str[i]=="h" and str[i+1]=="i" and i<x:
      c=c+1
  return c
