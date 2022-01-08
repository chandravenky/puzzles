#Solution1
def is_anagram(s, t):

  s_count = {}

  for letter in s:

    if letter in s_count:
      s_count[letter] = s_count[letter] + 1

    else:
      s_count[letter] = 1


  for letter in t:

    if letter in s_count:
      s_count[letter] = s_count[letter] -1

      if s_count[letter] == 0:
        del s_count[letter]

    else:
      return False

  if s_count:
    return False

  return True
