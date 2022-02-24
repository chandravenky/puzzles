#Problem 520



def detect_capital(word):
  
  if len(word) == 1:
    return True
        
  #first_capital
  if word[0].isupper():
    first_capital = 1
  else:
    first_capital = 0
  
  #second_capital
  if word[1].isupper():
    second_capital = 1
  else:
    second_capital = 0
      
  if first_capital == 0 and second_capital==1:
    return False
  
  for i in range(2, len(word)):
    if first_capital == 1 and second_capital == 1:
      if word[i].islower():
        return False
          
    if first_capital == 1 and second_capital == 0:
      if word[i].isupper():
        return False
          
    if first_capital ==0:
      if word[i].isupper():
        return False
          
  return True
