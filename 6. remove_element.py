
def remove_element(nums, val):

  holding_pointer = 0

  for i in range(0, len(nums)):

    if nums[i] != val:
      nums[holding_pointer] = nums[i]
      holding_pointer = holding_pointer +1
    
  return holding_pointer, nums
