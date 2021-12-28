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

# Tests
def max_sub_array_test():

  input_nums1 = [-2,1,-3,4,-1,2,1,-5,4]
  input_nums2 = [1]
  input_nums3 = [5,4,-1,7,8]

  actual_output_k1 = max_sub_array(input_nums1)
  actual_output_k2 = max_sub_array(input_nums2)
  actual_output_k3 = max_sub_array(input_nums3)

  return actual_output_k1==6, actual_output_k2 ==1, actual_output_k3==23

print(max_sub_array_test())

#For leetcode
class Solution(object):
    def maxSubArray(self, nums):
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
