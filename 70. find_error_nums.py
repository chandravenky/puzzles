#Problem 645

def find_error_nums(nums):

  store = {}
  running_sum = 0
  tot_expected_sum = len(nums)*(len(nums)+1)/2

  for i in range(0, len(nums)):

    if nums[i] not in store:
      store[nums[i]] = 1
      running_sum = running_sum + nums[i]
    else:
      num_occured_twice = nums[i]

  return [num_occured_twice, tot_expected_sum - running_sum]

#Add tests
def find_error_nums_test():

  input_nums1 = [1,2,2,4]
  input_nums2 = [1,1]

  expected_output1 = [2,3]
  expected_output2 = [1,2]

  return ( expected_output1 == find_error_nums(input_nums1), expected_output2 == find_error_nums(input_nums2) )

print(find_error_nums_test())
