def lone_sum(a, b, c):
  if a!=b and a!=c and b!=c:
    return a+b+c
  elif a!=b and a!=c and b==c:
    return a
  elif a==b and a!=c:
    return c
  elif a==c and a!=b:
    return b
  elif a==c and a==b and b==c:
    return 0