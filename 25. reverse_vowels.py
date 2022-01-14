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
