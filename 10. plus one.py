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


# Tests
def plus_one_test():

  input_array1 = [1,2,3]
  input_array2 = [4,3,2,1]
  input_array3 = [9]

  actual_output_k1 = plus_one(input_array1)
  actual_output_k2 = plus_one(input_array2)
  actual_output_k3 = plus_one(input_array3)

  return actual_output_k1==[1,2,4], actual_output_k2 ==[4,3,2,2], actual_output_k3==[1,0]

print(plus_one_test())
