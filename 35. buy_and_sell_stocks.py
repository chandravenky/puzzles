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
