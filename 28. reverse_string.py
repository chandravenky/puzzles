#Solution1
def reverse_string(input_string_array):

  traverse_length = len(input_string_array)//2
  
  for i in range(0, traverse_length):
    
    holding_pointer = input_string_array[i]

    input_string_array[i] = input_string_array[len(input_string_array) -1 - i]

    input_string_array[len(input_string_array) -1 - i] = holding_pointer

  return input_string_array
