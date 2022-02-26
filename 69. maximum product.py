#Problem 628

def maximum_product(nums):

  #2 cases - either all are positive
  #some are negative

  nums_sorted = sorted(nums)

  sum1 = nums_sorted[-1] * nums_sorted[-2] * nums_sorted[-3]
  sum2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[-1]

  return max(sum1, sum2)

#Add tests
def maximum_product_test():

  input_nums1 = [1,2,3]
  input_nums2 = [1,2,3,4]
  input_nums3 = [-1,-2,-3]

  expected_output1 = 6
  expected_output2 = 24
  expected_output3 = -6

  return ( expected_output1 == maximum_product(input_nums1), expected_output2 == maximum_product(input_nums2), expected_output3 == maximum_product(input_nums3) )

print(maximum_product_test())
  
#Final solution
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 cases - either all are positive
        #some are negative

        nums_sorted = sorted(nums)

        sum1 = nums_sorted[-1] * nums_sorted[-2] * nums_sorted[-3]
        sum2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[-1]

        return max(sum1, sum2)
