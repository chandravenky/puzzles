#Solution1
def plus_one(input_array):

  integer_form = ''.join([str(item) for item in input_array])

  incremented_num = int(integer_form) + 1

  split_form = [int(item) for item in str(incremented_num)]
    
  return split_form
