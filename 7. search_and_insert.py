#Solution 1
def search_and_insert(nums, target):

  for i in range(0, len(nums)):

    if target == nums[i]:
      return i

    elif target <nums[i]:
      return i
    
  return i+1

#Solution 2
def search_and_insert2(nums, target):
  start_index = 0
  half_index = len(nums)//2
  end_index = len(nums)

  while True:

      if target < nums[half_index]:
          end_index = half_index
          half_index = (start_index + half_index)//2

      elif target > nums[half_index]:
          start_index = half_index
          half_index = (half_index + end_index)//2

      if target == nums[half_index]:
          return half_index

      if (half_index == end_index or half_index == start_index) and target>nums[half_index]:

          return half_index +1

      if (half_index == end_index or half_index == start_index)  and target<nums[half_index]:
          return half_index

#Tests
def search_and_insert2_test():

  input_nums = [1,3,5,6]

  input_target1 = 5
  input_target2 = 2
  input_target3 = 7
  input_target4 = 0


  actual_output_k1 = search_and_insert2(input_nums, input_target1)
  actual_output_k2 = search_and_insert2(input_nums, input_target2)
  actual_output_k3 = search_and_insert2(input_nums, input_target3)
  actual_output_k4 = search_and_insert2(input_nums, input_target4)

  return actual_output_k1==2, actual_output_k2 ==1, actual_output_k3==4, actual_output_k4 == 0

print(search_and_insert2_test())



print(search_and_insert2([1,3,5,6], 5))
print(search_and_insert2([1,3,5,6], 2))
print(search_and_insert2([1,3,5,6], 7))
print(search_and_insert2([1,3,5,6], 0))
