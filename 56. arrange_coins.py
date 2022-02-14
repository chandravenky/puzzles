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


# #Tests
def arrange_coins_test():

  input_num1  = 5
  input_num2  = 8
  input_num3  = 1
  input_num4  = 2
  input_num5  = 3

  expected_result1 = 2
  expected_result2 = 3
  expected_result3 = 1
  expected_result4 = 1
  expected_result5 = 2

  return arrange_coins(input_num1) == expected_result1, arrange_coins(input_num2) == expected_result2, arrange_coins(input_num3) == expected_result3, arrange_coins(input_num4) == expected_result4, arrange_coins(input_num5) == expected_result5

print(arrange_coins_test())
