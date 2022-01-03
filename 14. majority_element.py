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
