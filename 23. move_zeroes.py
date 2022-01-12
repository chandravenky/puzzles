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
