def rob_house(nums):

  if len(nums)<3:

    return max(nums)

  cache = [nums[0], max(nums[0], nums[1])]

  for i in range(2, len(nums)):

    new_rob_amount = cache[-2] + nums[i]

    cache.append(max(new_rob_amount, cache[-1]))

  return cache[-1]

#Tests
def rob_house_test():

  input_array1= [1,2,3,1]
  input_array2= [2,7,9,3,1]
  input_array3= [2,1,1,2]

  expected_output1= 4
  expected_output2= 12
  expected_output3= 4

  result_tuple = ( expected_output1 == rob_house(input_array1), expected_output2 == rob_house(input_array2), expected_output3 == rob_house(input_array3) )

  return result_tuple

print(rob_house_test())
