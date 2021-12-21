def is_palindrome(input_number):

  input_number_text = str(input_number)

  reversed_text = input_number_text[::-1]

  return input_number_text == reversed_text

def test_is_palindrome():

  input_number1 = 45
  input_number2= 242

  output1 = is_palindrome(input_number1)
  output2 = is_palindrome(input_number2)

  return output1, output2

print(test_is_palindrome())

# For leetcode

class Solution(object):

    def isPalindrome(self, x):

      x_text = str(x)

      reversed_text = x_text[::-1]

      return x_text == reversed_text
