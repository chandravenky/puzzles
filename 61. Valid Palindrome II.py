#Problem 680

def valid_palindrome(s):

  for i in range(0, len(s)):

    string_to_analyze = s[:i] + s[i+1:]
    if string_to_analyze == string_to_analyze[::-1]:
      return True
  
  return False
