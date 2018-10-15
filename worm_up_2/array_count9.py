def array_count9(nums):
  c=0
  x=len(nums)
  for i in range(x):
    if nums[i]==9:
      c=c+1
      
  return c
print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))