def first_two(str):
  if len(str)>=2:
    return str[0]+str[1]
  elif len(str)<2:
    return str 
  else :
    return "empty string"
print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))
