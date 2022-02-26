#Problem 628

{{}}def maximum_product(nums):

  #2 cases - either all are positive
  #some are negative

  nums_sorted = sorted(nums)

  sum1 = nums_sorted[-1] * nums_sorted[-2] * nums_sorted[-3]
  sum2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[-1]

  return max(sum1, sum2)
