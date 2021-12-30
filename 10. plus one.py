#Solution1
def plus_one(input_array):

  integer_form = ''.join([str(item) for item in input_array])

  incremented_num = int(integer_form) + 1

  split_form = [int(item) for item in str(incremented_num)]
    
  return split_form

#Solution2
def plus_one_2(input_array):
  
  num = 0

  for i in range(0, len(input_array)):

    num = num + input_array[i]*(10**(len(input_array) - i-1))

  num = num +1

  return list(str(num))
