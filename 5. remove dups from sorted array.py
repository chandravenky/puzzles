class Solution(object):
    def removeDuplicates(self, input_array):
        holding_pointer = 1
        for i in range(0, len(input_array)-1):

            if input_array[i]!=input_array[i+1]:

                input_array[holding_pointer] = input_array[i+1]
                holding_pointer = holding_pointer + 1

        return holding_pointer
