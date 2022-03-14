#Problem 1323

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        max_num = num
        num_string = list(str(num))
        
        for i in range(0, len(num_string)):
            new_string = copy.deepcopy(num_string)

            if new_string[i]=='6':
                new_string[i] = '9'
                
            else:
                new_string[i] = '6'

            if int(''.join(new_string))> max_num:
                max_num = int(''.join(new_string))
                
        return max_num
