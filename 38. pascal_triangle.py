def pascal_triangle(n):

  result_list = [[1], [1,1], [1,2,1]]

  if n<3:
    return result_list[:n]

  for i in range(3, n):

    num_elements_in_pattern = (i)//2
    
    calculated_list = []

    for j in range(1, num_elements_in_pattern+1):

      calculated_list.append(result_list[-1][j] + result_list[-1][j-1])

    if i%2!=0:

      current_row_res = [1] + calculated_list + calculated_list[::-1] + [1]

    else:
      current_row_res = [1] + calculated_list + calculated_list[:len(calculated_list)-1][::-1] + [1]
    
    result_list.append(current_row_res)

  return result_list

#Add tests
def pascal_triangle_test():

  input_n1 = 1
  input_n2 = 2
  input_n3 = 3
  input_n4 = 4
  input_n5 = 5
  input_n6 = 6
  input_n7 = 7

  expected_output1 = [[1]]
  expected_output2 = [[1], [1, 1]]
  expected_output3 = [[1], [1, 1], [1, 2, 1]]
  expected_output4 = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
  expected_output5 = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
  expected_output6 = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
  expected_output7 = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]

  actual_output1 = pascal_triangle(input_n1)
  actual_output2 = pascal_triangle(input_n2)
  actual_output3 = pascal_triangle(input_n3)
  actual_output4 = pascal_triangle(input_n4)
  actual_output5 = pascal_triangle(input_n5)
  actual_output6 = pascal_triangle(input_n6)
  actual_output7 = pascal_triangle(input_n7)

  return actual_output1== expected_output1, actual_output2== expected_output2, actual_output3== expected_output3, actual_output4== expected_output4, actual_output5== expected_output5, actual_output6== expected_output6, actual_output7== expected_output7

print(pascal_triangle_test())

#Leetcode
class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result_list = [[1], [1,1], [1,2,1]]
        
        
        if n<3:
            return result_list[:n]

        for i in range(3, n):

            num_elements_in_pattern = (i)//2

            calculated_list = []

            for j in range(1, num_elements_in_pattern+1):

                calculated_list.append(result_list[-1][j] + result_list[-1][j-1])


            if i%2!=0:
                print("yes")
                current_row_res = [1] + calculated_list + calculated_list[::-1] + [1]

            else:
                current_row_res = [1] + calculated_list + calculated_list[:len(calculated_list)-1][::-1] + [1]

            result_list.append(current_row_res)

        return result_list
