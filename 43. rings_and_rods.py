# Solution
def count_points(input_string):

  ring_tracker = {}

  for i in range(0, len(input_string),2):

    ring_color = input_string[i]
    rod_number = input_string[i+1]

    if rod_number not in ring_tracker:
      ring_tracker[rod_number] = [ring_color]

    else:
      
      if ring_color not in ring_tracker[rod_number]:

        ring_tracker[rod_number].append(ring_color )

  #filter for values with length ==3
  filtered_ring_tracker = { key:value for key, value in ring_tracker.items() if len(value)==3}

  return len(filtered_ring_tracker.keys())

#Tests
def count_points_test():

  input_string1 = "B0B6G0R6R0R6G9"
  input_string2 = "G4"

  expected_output1 = 1
  expected_output2 = 0

  actual_output1 = count_points(input_string1)
  actual_output2 = count_points(input_string2)

  return expected_output1 == actual_output1, expected_output2 == actual_output2

print(count_points_test())

#Leetcode
class Solution(object):
  def countPoints(self, input_string):
    """
    :type rings: str
    :rtype: int
    """
    ring_tracker = {}

    for i in range(0, len(input_string),2):

      ring_color = input_string[i]
      rod_number = input_string[i+1]


      if rod_number not in ring_tracker:
        ring_tracker[rod_number] = [ring_color]

      else:

        if ring_color not in ring_tracker[rod_number]:

          ring_tracker[rod_number].append(ring_color)

    #filter for values with length ==3
    filtered_ring_tracker = { key:value for key, value in ring_tracker.items() if len(value)==3}

    return len(filtered_ring_tracker.keys())
