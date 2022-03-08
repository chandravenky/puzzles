#Problem 819
import re

def most_common_word(paragraph, banned):

  store = {}
  paragraph = paragraph.lower()
  paragraph = re.sub(r'[^\w\s]',' ',paragraph)
  
  paragraph_list = paragraph.split()

  banned = banned if len(banned) else ['']

  for word in paragraph_list:
      
    if word in banned:
      pass
    
    elif word in store:
      store[word] = store[word] + 1
        
    else:
      store[word] = 1
  
  most_frequent_value = max(store.values())
  most_frequent_item = [key for key, value in store.items() if value == most_frequent_value]
  
  return most_frequent_item[0]

def most_common_word_test():

  input_paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
  input_paragraph2 = "a."
  input_paragraph3 = "a, a, a, a, b,b,b,c, c"
  input_paragraph4 = "abc abc? abcd the jeff!"

  input_banned1 = ["hit"]
  input_banned2 = ["b"]
  input_banned3 = ["a"]
  input_banned4 = ["abc", "abcd", "jeff"]

  expected_output1 = "ball"
  expected_output2 = "a"
  expected_output3 = "b"
  expected_output4 = "the"

  return ( expected_output1 == most_common_word(input_paragraph1, input_banned1), expected_output2 == most_common_word(input_paragraph2, input_banned2), expected_output3 == most_common_word(input_paragraph3, input_banned3), expected_output4 == most_common_word(input_paragraph4, input_banned4) )

print(most_common_word_test())
