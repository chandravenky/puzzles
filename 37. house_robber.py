def rob_house(nums):

  if len(nums)<3:

    return max(nums)

  cache = [nums[0], max(nums[0], nums[1])]

  for i in range(2, len(nums)):

    new_rob_amount = cache[-2] + nums[i]

    cache.append(max(new_rob_amount, cache[-1]))

  return cache[-1]
