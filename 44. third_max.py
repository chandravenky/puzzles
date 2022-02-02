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
