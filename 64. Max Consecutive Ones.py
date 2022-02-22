#Problem 485


def max_consecutive_ones(nums):

  max_count =0
  count = 0
  prev = 0
  
  if nums == [1]:
    return 1
    
  for i in range(0, len(nums)):
    print(i)
    if nums[i]==1:
      
      if prev==1:
        count=count+1

      else:
        count = 1
      prev = 1

    else:
      prev= 0 

    if count> max_count:
      max_count = count

  return max_count
