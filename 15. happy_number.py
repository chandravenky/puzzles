
def happy_number(input_num):

  def sum_square(digit):

    result =0

    for each_digit in str(digit):

      result = result + int(each_digit)**2

    return result
  
  square_sum = 0

  cycle_list = []

  while square_sum !=1:

    square_sum = sum_square(input_num)

    input_num = square_sum

    if input_num == 1:
      return True

    if input_num in cycle_list:
      return False

    else:
      cycle_list.append(input_num)
