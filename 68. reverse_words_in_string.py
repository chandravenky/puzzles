#Problem 151

def reverse_words(s):

  words_list = s.split()
  
  for i in range(0, len(words_list)//2):
    
    hold_word = words_list[i]
    
    words_list[i] = words_list[len(words_list)-1-i]
    words_list[len(words_list)-1-i] = hold_word
  
  return ' '.join(words_list)

#Add tests
def reverse_words_test():

  input_s1 = "the sky is blue"
  input_s2 = "  hello world  "
  input_s3 = "a good   example"

  expected_output1 = "blue is sky the"
  expected_output2 = "world hello"
  expected_output3 = "example good a"

  return ( expected_output1 == reverse_words(input_s1), expected_output2 == reverse_words(input_s2), expected_output3 == reverse_words(input_s3) )

print(reverse_words_test())
