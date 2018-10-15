def extra_end(str):
  if len(str)>=2 :
    x=str[-2:]
    return x+x+x
print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))