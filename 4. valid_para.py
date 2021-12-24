
def valid_parant(input_string):

  open_close_map = {
    '(': ')',
    '[': ']',
    '{': '}'
  }

  open_close_array=[]

  #odd can simply be removed
  if len(input_string)%2 !=0 or len(input_string)==0:
    return False

  for i in range(0, len(input_string)):

    #if something gets opened, it is stored in order
    if input_string[i] in open_close_map.keys():
      open_close_array.append(input_string[i])

    #if a closing is encountered, it must follow order
    elif input_string[i] in open_close_map.values() and open_close_array:
      if input_string[i] != open_close_map[open_close_array.pop()]:
        return False
    
    #if only closing is encountered, return False
    else:
      return False
  
  #if something remains unclosed, return False
  if open_close_array:
    return False
  
  #if everything is closed, return True
  return True

def test_valid_parant():

  input_string1 = "()"
  input_string2 = "()("
  input_string3 = ""
  input_string4 = "()[]{}"
  input_string5 = "{[]}"
  input_string6 = "([)]"
  input_string7 = "(("
  input_string8 = "){"

  output1 = valid_parant(input_string1) == True
  output2 = valid_parant(input_string2) == False
  output3 = valid_parant(input_string3) == False
  output4 = valid_parant(input_string4) == True
  output5 = valid_parant(input_string5) == True
  output6 = valid_parant(input_string6) == False
  output7 = valid_parant(input_string7) == False
  output8 = valid_parant(input_string8) == False

  return output1, output2, output3, output4, output5, output6, output7, output8

print(test_valid_parant())
