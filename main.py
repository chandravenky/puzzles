
def is_palindrome_2(input_number):

  if input_number == 0:
    return True

  elif input_number < 0 or input_number %10 == 0:

    return False

  reverted_number= 0

  while input_number > reverted_number:

    reverted_number = reverted_number * 10 + input_number%10

    input_number = input_number//10

  return input_number == reverted_number or input_number == reverted_number//10

def test_is_palindrome2():

  input_number1 = 45
  input_number2= 2442
  input_number3 = 242

  output1 = is_palindrome_2(input_number1)
  output2 = is_palindrome_2(input_number2)
  output3 = is_palindrome_2(input_number3)

  return output1, output2, output3

print(test_is_palindrome2())
