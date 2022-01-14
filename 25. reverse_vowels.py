#Solution1
def reverse_vowels(input_string):

  vowel_string = ''
  index_string = []
  input_string = list(input_string)

  for index, letter in enumerate(input_string):

    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:

      vowel_string = vowel_string + letter

      index_string.append(index)

  #Reverse the vowel string
  vowel_string = list(vowel_string[::-1])

  for i in range(0, len(index_string)):

  
    input_string[index_string[i]] = vowel_string[i]

  return ''.join(input_string)

#Tests
def reverse_vowels_test():

  input_string1 = "hello"
  input_string2 = "leetcode"
  input_string3 = "aA"
  input_string4 = "A man, a plan, a canal: Panama"

  
  expected_output1 = "holle"
  expected_output2 = "leotcede"
  expected_output3 = "Aa"
  expected_output4 = "a man, a plan, a canal: PanamA"

  return ( expected_output1 == reverse_vowels(input_string1), expected_output2 == reverse_vowels(input_string2), expected_output3 == reverse_vowels(input_string3), expected_output4 == reverse_vowels(input_string4) )

print(reverse_vowels_test())
