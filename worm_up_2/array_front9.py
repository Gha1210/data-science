def array_front9(nums):
  
  if (len(nums)) >= 4 :
    for i in range(4) :
      if nums[i] == 9 :
        return True
  elif (len(nums))<4:
    for k in range(len(nums)):
      if nums[k]==9:
        return True
  return False
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))