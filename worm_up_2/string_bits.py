def string_bits(str):
   x=len(str)
   l=""
   i=0
   while i<x :
       l=l+str[i]
       i=i+2
   return l
print(string_bits('Hello') )
print(string_bits('Hi') )
print(string_bits('Heeololeo'))
