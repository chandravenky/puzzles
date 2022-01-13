#Solution1
def missing_number(input_array):

  superset_list = list(range(0,len(input_array)+1))
  # print(superset_list)

  return list(set(superset_list)-set(input_array))[0]

#Best solution with O(1) space
def missing_number2(input_array):
    """
    :type nums: List[int]
    :rtype: int
    """

    tot_sum = (len(input_array)*(len(input_array) + 1))/2
    
    for i in input_array:
        
        tot_sum = tot_sum -i
        
    return tot_sum
