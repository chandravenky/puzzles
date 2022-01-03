#Solution1
def majority_element(nums):

  threshold = len(nums)/2
  cnt_dict = {}

  if len(nums) == 1:
    return nums[0]

  for num in nums:

    if num in cnt_dict:
      cnt_dict[num] = cnt_dict[num] + 1
      if cnt_dict[num]>=threshold:
        return num

    else:
      cnt_dict[num] = 1

#Better solution with O(1) solution

#Boyer-Moore algorithm
def majority_element_2(nums):

  count = 0
  res = nums[0]

  for num in nums[1:]:

    if num != res:
      
      count = count-1
      
      if count <0:
        count = 0
        res = num
    
    else:
      count = count + 1

  return res
