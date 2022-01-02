# #Solution - Best
def excel_sheet_column_num(input_col_num):

  map_dict = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''


  if input_col_num <=26:
      return map_dict[input_col_num]

  else:

      while input_col_num>0:

          input_col_num, remainder = divmod(input_col_num,26)

          if remainder == 0:

              remainder = 26
              input_col_num = input_col_num -1
          result = map_dict[remainder] + result

  return result

#Less readable - uses original index
def excel_sheet_column_num_2(input_col_num):

  map_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''

  if input_col_num <=26:
    return map_dict[input_col_num-1]

  else:

    while input_col_num>0:

      input_col_num, remainder = divmod(input_col_num,26)
      
      if remainder == 0:

        remainder = 26
        input_col_num = input_col_num -1
      
      result = map_dict[remainder-1] + result

  return result

#Tests
def excel_sheet_column_num_test():

  input_number1= 1
  input_number2= 28
  input_number3= 701
  input_number4= 2147483647

  expected_output1 = "A"
  expected_output2 = "AB"
  expected_output3 = "ZY"
  expected_output4 = "FXSHRXW"

  result_tuple1 = (excel_sheet_column_num(input_number1) == expected_output1, excel_sheet_column_num(input_number2) == expected_output2, excel_sheet_column_num(input_number3) == expected_output3, excel_sheet_column_num(input_number4) == expected_output4)

  result_tuple2 = (excel_sheet_column_num_2(input_number1) == expected_output1, excel_sheet_column_num_2(input_number2) == expected_output2, excel_sheet_column_num_2(input_number3) == expected_output3, excel_sheet_column_num_2(input_number4) == expected_output4)
  
  return result_tuple1, result_tuple2

print(excel_sheet_column_num_test())

#Leetcode
class Solution(object):
  def convertToTitle(self, input_col_num):
      """
      :type columnNumber: int
      :rtype: str
      """
      map_dict = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      result = ''


      if input_col_num <=26:
          return map_dict[input_col_num]

      else:

          while input_col_num>0:

              input_col_num, remainder = divmod(input_col_num,26)

              if remainder == 0:

                  remainder = 26
                  input_col_num = input_col_num -1
              result = map_dict[remainder] + result

      return result
