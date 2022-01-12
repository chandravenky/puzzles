#Solution1
def move_zeroes(input_array):

  current_pointer = 0

  for i in range(0, len(input_array)):
    
  
    if input_array[i] == 0 and current_pointer==i:
      current_pointer = i
    
    elif input_array[i] != 0:

      swap_value = input_array[current_pointer]
      input_array[current_pointer] = input_array[i]
      input_array[i] = swap_value
      current_pointer= current_pointer + 1

    else:
      pass
    
  return input_array

# Tests
def move_zeroes_test():

  input_array1 = [0,1,0,3,12]
  input_array2 = [0]
  input_array3 = [2,1]
  input_array4 = [0,8]
  input_array5 = [1,0,0,4]


  expected_output1 = [1,3,12,0,0]
  expected_output2 = [0]
  expected_output3 = [2,1]
  expected_output4 = [8,0]
  expected_output5 = [1,4,0,0]


  return move_zeroes(input_array1) == expected_output1, move_zeroes(input_array2) == expected_output2, move_zeroes(input_array3) == expected_output3, move_zeroes(input_array4) == expected_output4, move_zeroes(input_array5) == expected_output5

print(move_zeroes_test())
