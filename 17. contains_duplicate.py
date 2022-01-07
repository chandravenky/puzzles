
def contains_duplicate(input_array, k):

  map_dict = {}

  for index, value in enumerate(input_array):

    if value in map_dict:
      
      if index - map_dict[value] <=k:

        return True
      
      map_dict[value] = index
    
    else:
      map_dict[value] = index

  return False

#Tests
def contains_duplicate_test():

  input_array1 = [1,2,3,1]
  input_array2 = [1,0,1,1]
  input_array3 = [1,2,3,1,2,3]

  return ( contains_duplicate(input_array1, 3) == True, contains_duplicate(input_array2, 1) == True, contains_duplicate(input_array3, 2) == False )

print(contains_duplicate_test())

# #Leetcode
class Solution(object):
  def containsNearbyDuplicate(self, input_array, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    map_dict = {}

    for index, value in enumerate(input_array):

      if value in map_dict:

        if index - map_dict[value] <=k:

          return True

        map_dict[value] = index

      else:
        map_dict[value] = index

    return False
