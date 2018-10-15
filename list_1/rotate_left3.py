def rotate_left3(nums):
  x=[1,2,3]
  if len(nums)==3:
    x[0]=nums[1]
    x[1]=nums[2]
    x[2]=nums[0]
    return x
print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
