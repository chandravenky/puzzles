
def longest_prefix(input_string_array):

  string_lengths = [len(string) for string in input_string_array]
  
  output = ""
  for i in range(0, min(string_lengths)):

    string_to_check = input_string_array[0][i]
    
    present = 1

    for string in input_string_array[1:]:
      

      if string[i] == string_to_check:
        
        present = present + 1

      else:

        return output

    if present == len(input_string_array):

      output = output + string_to_check

  return output

def test_longest_prefix():

  input_string_array = ["dog","racecar","car"]

  output_val = longest_prefix(input_string_array)

  return output_val

print(test_longest_prefix())
