def num_different_integers(s):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    s = s + "x"
    num_list = list("0123456789")
    str_current = ""
    store = {}
    
    for i in range(0, len(s)):

      if s[i] not in num_list:
        if len(str_current)>0:
          store[str_current] = 1

          str_current = ""
        
        else:
          pass

      else:
        if s[i] != "0":
          str_current = str_current + s[i]

        else:
          if len(str_current)>0:
            str_current = str_current + s[i]
          
          else:
            if i+1<len(s):
              if s[i+1] not in num_list:
                str_current = str_current + s[i]
            
            else:
              pass

    if len(str_current)>0:
      store[str_current] = 1

    return len(store.keys())

#Solution 2 - Better solution
def num_different_integers2(s):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i=0
    num_list = list("0123456789")
    store = {}
    str_current = ""
    
    while i < len(s):
      
      if s[i] not in num_list:
        i = i+1

      else:
        j=i
        while j<len(s) and s[j] in num_list:
          
          str_current = str_current + s[j]
          j = j+1
          
        store[str_current] = 1
        str_current = ""
        i=j

    nums = [int(item) for item in store.keys()]
    return len(set(nums))

def num_different_integers_test():

  input_string1 = "a123bc34d8ef34"
  input_string2 = "leet1234code234"
  input_string3 = "a1b01c001"
  input_string4 = "gi851a851q8510v"
  input_string5 = "0a0"
  input_string6 = "a0"
  input_string7 = "0a"
  input_string8 = "0"

  expected_output1 = 3
  expected_output2 = 2
  expected_output3 = 1
  expected_output4 = 2
  expected_output5 = 1
  expected_output6 = 1
  expected_output7 = 1
  expected_output8 = 1

  return ( expected_output1 == num_different_integers(input_string1), expected_output2 == num_different_integers(input_string2), expected_output3 == num_different_integers(input_string3), expected_output4 == num_different_integers(input_string4), expected_output5 == num_different_integers(input_string5), expected_output6 == num_different_integers(input_string6), expected_output7 == num_different_integers(input_string7), expected_output8 == num_different_integers(input_string8) )

print(num_different_integers_test())

class Solution(object):
    def numDifferentIntegers(self, s):
        """
        :type word: str
        :rtype: int
        """
        s = s + "x"
        num_list = list("0123456789")
        str_current = ""
        store = {}

        for i in range(0, len(s)):

            if s[i] not in num_list:
                if len(str_current)>0:
                    store[str_current] = 1

                    str_current = ""

                else:
                    pass

            else:
                if s[i] != "0":
                    str_current = str_current + s[i]

                else:
                    if len(str_current)>0:
                        str_current = str_current + s[i]

                    else:
                        if i+1<len(s):
                            if s[i+1] not in num_list:
                                str_current = str_current + s[i]

                        else:
                            pass

        if len(str_current)>0:
            store[str_current] = 1

        return len(store.keys())
