#Solution 1
def length_last_word(input_string):

  words = input_string.split()
    
  return len(words[-1])

# # Tests
def length_last_word_test():

  input_string1 = "Hello World"
  input_string2 = "   fly me   to   the moon  "
  input_string3 = "luffy is still joyboy"

  actual_output_k1 = length_last_word(input_string1)
  actual_output_k2 = length_last_word(input_string2)
  actual_output_k3 = length_last_word(input_string3)

  return actual_output_k1==5, actual_output_k2 ==4, actual_output_k3==6

print(length_last_word_test())
