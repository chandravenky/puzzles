
def excel_sheet_col_num(input_col_name):

  input_col_name = input_col_name.lower()

  num = 0

  for i in range(0, len(input_col_name)):

    num = num + ((26** (len(input_col_name)-i-1))*(ord(input_col_name[i])-96))

  return num

#Tests
def excel_sheet_col_num_test():

  input_col_name1 = 'A'
  input_col_name2 = 'ZY'
  input_col_name3 = 'AAA'
  input_col_name4 = 'BAA'
  input_col_name5= 'FXSHRXW'

  expected_output1= 1 
  expected_output2= 701
  expected_output3= 703
  expected_output4= 1379
  expected_output5= 2147483647

  return ( excel_sheet_col_num(input_col_name1) == expected_output1, excel_sheet_col_num(input_col_name2) == expected_output2, excel_sheet_col_num(input_col_name3) == expected_output3, excel_sheet_col_num(input_col_name4) == expected_output4, excel_sheet_col_num(input_col_name5) == expected_output5 )

print(excel_sheet_col_num_test())


#Submission
class Solution(object):
  def titleToNumber(self, input_col_name):
    """
    :type columnTitle: str
    :rtype: int
    """
    input_col_name = input_col_name.lower()

    num = 0

    for i in range(0, len(input_col_name)):

        # print(i, input_col_name[i], ord(input_col_name[i])-96)

        num = num + ((26** (len(input_col_name)-i-1))*(ord(input_col_name[i])-96))

    return num
    
