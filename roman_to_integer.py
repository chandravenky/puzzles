
def roman_to_integer(input_roman):

  roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  output =0
  i =0

  while i< len(input_roman):

    if i < len(input_roman)-1 and roman_values[input_roman[i]] < roman_values[input_roman[i+1]]:
      output =  output + roman_values[input_roman[i+1]] - roman_values[input_roman[i]]

      i = i + 2
    
    else:

      output = output + roman_values[input_roman[i]]
      i= i+1

  return output

def test_roman_to_integer():

  input_number1 = "III"
  input_number2= "LVIII"
  input_number3 = "MCMXCIV"

  output1 = roman_to_integer(input_number1)
  output2 = roman_to_integer(input_number2)
  output3 = roman_to_integer(input_number3)

  return output1, output2, output3

print(test_roman_to_integer())
