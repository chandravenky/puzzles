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
