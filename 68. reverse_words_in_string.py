#Problem 151

def reverse_words(s):

  words_list = s.split()
  
  for i in range(0, len(words_list)//2):
    
    hold_word = words_list[i]
    
    words_list[i] = words_list[len(words_list)-1-i]
    words_list[len(words_list)-1-i] = hold_word
  
  return ' '.join(words_list)
