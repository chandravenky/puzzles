def arrange_coins(n):

    start = 0
    end = n

    while start<=end:
        
      mid = (start+end)//2
      
      tot_sum = mid*(mid+1)//2
      
      if tot_sum > n:
          
        end = mid - 1
          
      elif tot_sum <n:
        start = mid + 1
          
      else:
        return mid
        
    return end
