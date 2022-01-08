
def contains_duplicate(input_array):

  map_dict = {}

  for i in range(0, len(input_array)):

    if input_array[i] in map_dict:
      return True
    
    else:
      map_dict[input_array[i]] = 1

  return False

#Tests
def contains_duplicate_test():

  input_array1 = [1,2,3,1]
  input_array2 = [1,2,3,4]
  input_array3 = [1,1,1,3,3,4,3,2,4,2]
  input_array4 = [1]
  input_array5 = []

  return ( contains_duplicate(input_array1) == True, contains_duplicate(input_array2) == False, contains_duplicate(input_array3) == True, contains_duplicate(input_array4) == False, contains_duplicate(input_array5) == False )

print(contains_duplicate_test())

#Leetcode
class Solution(object):
  def containsDuplicate(self, input_array):
    """
    :type nums: List[int]
    :rtype: bool
    """
    map_dict = {}

    for i in range(0, len(input_array)):

      if input_array[i] in map_dict:
        return True

      else:
        map_dict[input_array[i]] = 1

    return False
