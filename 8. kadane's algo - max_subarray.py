#Solution 1
def max_sub_array(nums):

  highest_sum = nums[0]
  current_sum = nums[0]

  for i in range(1, len(nums)):
    
    if current_sum + nums[i] > nums[i]:
      current_sum = current_sum + nums[i]

      if current_sum > highest_sum:
        highest_sum = current_sum

    else:
      current_sum = nums[i]

      if current_sum > highest_sum:
        highest_sum = current_sum
    
  return highest_sum
