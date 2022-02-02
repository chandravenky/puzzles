# Solution
def third_max(nums):

  first_max = -2147483649
  second_max = -2147483649
  third_max = -2147483649

  for i in range(0, len(nums)):

    if nums[i] > max(first_max, second_max, third_max):
      third_max = second_max
      second_max = first_max
      first_max = nums[i]

    elif nums[i]> max(third_max, second_max) and nums[i]<first_max:
      third_max = second_max
      second_max = nums[i]

    elif nums[i]> third_max and nums[i]< min(second_max, first_max):
      third_max = nums[i]

    else:
      pass

    # print(i, first_max, second_max, third_max)

  if second_max==-2147483649 or third_max==-2147483649:
    third_max = first_max

  return third_max



#Tests
def third_max_test():


  input_array1 =  [1,2,3,4,5,4,3,2,1]
  input_array2 =  [3,2,1]
  input_array3 =  [2,2,3,1]
  input_array4 =  [1,2,2,5,3,5]
  input_array5 =  [1,2,-2147483648]
  input_array6 =  [1,2]
  input_array7 =  [2,2,2,2,2,2,2]

  expected_output1 = 3
  expected_output2 = 1
  expected_output3 = 1
  expected_output4 = 2
  expected_output5 = -2147483648
  expected_output6 = 2
  expected_output7 = 2

  actual_output1 = third_max(input_array1)
  actual_output2 = third_max(input_array2)
  actual_output3 = third_max(input_array3)
  actual_output4 = third_max(input_array4)
  actual_output5 = third_max(input_array5)
  actual_output6 = third_max(input_array6)
  actual_output7 = third_max(input_array7)

  return ( expected_output1 == actual_output1, expected_output2 == actual_output2, expected_output3 == actual_output3, expected_output4 == actual_output4, expected_output5 == actual_output5, expected_output6 == actual_output6, expected_output7 == actual_output7 )

print(third_max_test())
