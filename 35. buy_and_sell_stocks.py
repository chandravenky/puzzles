def max_profit(nums):

  if len(nums)<3:

    return max(nums)

  cache = [0]
  min_buy = nums[0]

  for i in range(1, len(nums)):

    # print(i, nums[i], min_buy, cache)

    if nums[i] < min_buy:
      min_buy = nums[i]
    
    profit = nums[i]-min_buy

    cache.append(max(profit, cache[-1]))

  return cache[-1]

#Tests
def max_profit_test():

  input_array1= [7,1,5,3,6,4]
  input_array2=[7,6,4,3,1]
  input_array3= [2,1,1,2]

  expected_output1= 5
  expected_output2= 0
  expected_output3= 1

  result_tuple = ( expected_output1 == max_profit(input_array1), expected_output2 == max_profit(input_array2), expected_output3 == max_profit(input_array3) )

  return result_tuple

print(max_profit_test())

#Leetcode
class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit=0
        min_buy = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < min_buy:
                min_buy = nums[i]

            profit = nums[i]-min_buy
            
            if profit>max_profit:
                max_profit = profit

        return max_profit
        
