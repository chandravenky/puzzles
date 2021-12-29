#Solution 1
def length_last_word(input_string):

  words = input_string.split()
    
  return len(words[-1])
