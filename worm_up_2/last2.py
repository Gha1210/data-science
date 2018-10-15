def last2(str):
  f=len(str)
  if f < 2:
    return 0
  c = 0 
  l = str[-2:]
  u=(len(str)-2)
  for i in range(u):
    k = str[i]+str[i+1]
    if k == l:
      c = c + 1
  return c
print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
