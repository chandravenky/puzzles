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
