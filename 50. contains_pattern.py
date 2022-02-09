def contains_pattern(arr, m, k):

  pattern = {}

  for i in range(0, len(arr)):

    if arr[i:i+m] == arr[i+m:i+2*m]:
      
      pattern_string = ''.join(str(v) for v in arr[i:i+m])

      if pattern_string in pattern and pattern_string:
        
        pattern[pattern_string] = pattern[pattern_string] + 1
      
      else:
        pattern[pattern_string] = 2

    else:
      pattern = { key:value for key, value in pattern.items() if value>=k}

  #filter for results
  result =  { key:value for key, value in pattern.items() if value>=k}

  if result:
    return True
  
  return False

#Tests

def contains_pattern_test():

  input_array1 = [1,2,4,4,4,4]
  input_array2 = [1,2,1,2,1,1,1,3]
  input_array3 = [1,2,1,2,1,3]
  input_array4 = [6,3,5,5,5,5,1,5,6,2,5,1,2,5,3,5,1,3,5,5,6,4,1,2]
  input_array5 = [3,2,2,1,2,2,1,1,1,2,3,2,2]

  input_m1 = 1
  input_m2 = 2
  input_m3 = 2
  input_m4 = 1
  input_m5 = 3

  input_k1 = 3
  input_k2 = 2
  input_k3 = 3
  input_k4 = 5
  input_k5 = 2

  expected_result = ( contains_pattern(input_array1, input_m1, input_k1),
  contains_pattern(input_array2, input_m2, input_k2),
  contains_pattern(input_array3, input_m3, input_k3),
  contains_pattern(input_array4, input_m4, input_k4),
  contains_pattern(input_array5, input_m5, input_k5) )

  actual_result = ( True, True, False, False, True )


  return expected_result == actual_result

print(contains_pattern_test())

#Leetcode

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        pattern = {}

        for i in range(0, len(arr)):


            if arr[i:i+m] == arr[i+m:i+2*m]:

            

                pattern_string = ''.join(str(v) for v in arr[i:i+m])

                if pattern_string in pattern:

                    pattern[pattern_string] = pattern[pattern_string] + 1

                else:
                    pattern[pattern_string] = 2
            else:
                pattern = { key:value for key, value in pattern.items() if value>=k}

        # print('outer', pattern)
        #filter for results
        result =  { key:value for key, value in pattern.items() if value>=k}

        if result:
            return True

        return False
