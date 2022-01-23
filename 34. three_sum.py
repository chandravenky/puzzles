#Best solution
def three_sum(nums):

  if len(nums) <3:
    return []

  #sort O(n)
  nums_sorted = sorted(nums)
  
  result_list = []

  for i in range(0, len(nums_sorted)-2):
    
    if i ==0 or (i >0 and nums_sorted[i] != nums_sorted[i-1]):
      target = 0 - nums_sorted[i]
      first_pointer = i+1
      second_pointer = len(nums_sorted) - 1

      while first_pointer < second_pointer:
       
        if nums_sorted[first_pointer] + nums_sorted[second_pointer]==target:
          
          result_list.append([nums_sorted[i], nums_sorted[first_pointer], nums_sorted[second_pointer]])

          while first_pointer< second_pointer:
            
            if nums_sorted[first_pointer] == nums_sorted[first_pointer +1]:
              first_pointer = first_pointer + 1
            
            elif nums_sorted[second_pointer] == nums_sorted[second_pointer - 1]:
              second_pointer = second_pointer - 1
            
            else:
              break

          first_pointer = first_pointer + 1
          second_pointer = second_pointer - 1

        elif nums_sorted[first_pointer] + nums_sorted[second_pointer]>target:
          
          second_pointer = second_pointer-1

        elif nums_sorted[first_pointer] + nums_sorted[second_pointer]<target:
          
          first_pointer = first_pointer +1
    
  return result_list

#Tests
def three_sum_test():

  input_array1 = ([-1,0,1,2,-1,-4])
  input_array2 = ([])
  input_array3 = ([0])
  input_array4 = ([-1,0,1,2,-1,-4,-2,-3,3,0,4])

  expected_output1 = [[-1, -1, 2], [-1, 0, 1]]
  expected_output2 = []
  expected_output3 = []
  expected_output4 = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

  return ( expected_output1 == three_sum(input_array1),
           expected_output2 == three_sum(input_array2),
           expected_output3 == three_sum(input_array3),
           expected_output4 == three_sum(input_array4)   
              )

print(three_sum_test())
