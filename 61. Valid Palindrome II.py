#Problem 680

def valid_palindrome(s):

  for i in range(0, len(s)):

    string_to_analyze = s[:i] + s[i+1:]
    if string_to_analyze == string_to_analyze[::-1]:
      return True
  
  return False

#Tests
def valid_palindrome_test():

  input_s1 = "aba"
  input_s2 = "abca"
  input_s3 = "abc"

  expected_output1 = True
  expected_output2 = True
  expected_output3 = False

  return ( expected_output1 == valid_palindrome(input_s1), expected_output2 == valid_palindrome(input_s2), expected_output3 == valid_palindrome(input_s3) )

print(valid_palindrome_test())
