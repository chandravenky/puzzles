
def remove_element(nums, val):

  holding_pointer = 0

  for i in range(0, len(nums)):

    if nums[i] != val:
      nums[holding_pointer] = nums[i]
      holding_pointer = holding_pointer +1
    
  return holding_pointer, nums

def remove_element_test():

  input_nums1 = [3,2,2,3]
  input_nums2 = [0,1,2,2,3,0,4,2]

  input_k1 = 3
  input_k2 = 2

  expected_output_k1= 2
  expected_output_k2= 5
  actual_output_k1, _ = remove_element(input_nums1, input_k1)
  actual_output_k2, _ = remove_element(input_nums2, input_k2)

  return actual_output_k1 == expected_output_k1, actual_output_k2 == expected_output_k2
