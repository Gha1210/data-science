def big_diff(nums):
  max=0
  
  for i in nums:
    if i>max:
      max=i
  min=max
  for o in nums:
    if o<min :
      min=o
  return max-min
