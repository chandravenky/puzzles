#Problem 748

#Descriptive solution

def shortest_completing_word(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    store = {}
    shortest_length = 9999999999
    licensePlate = licensePlate.lower()
    licensePlate = list(licensePlate)
    output = ""
    
    for i in range(0, len(licensePlate)):
        
      try:
        int_converted = int(licensePlate[i])
      
      except:
        if licensePlate[i].strip() == '':
          pass
        elif licensePlate[i] not in store:
          store[licensePlate[i]] = 1
        else:
          store[licensePlate[i]] = store[licensePlate[i]] + 1
              
    for each_word in words:
        
      interim_store = {}
      
      for i in range(0, len(each_word)):
          
        if each_word[i] not in interim_store:
          interim_store[each_word[i]] = 1
        else:
          interim_store[each_word[i]] = interim_store[each_word[i]] + 1
                
      #Compare
      try:
        result = {key: value for key, value in store.items() if store[key] <= interim_store[key]}
          
        if len(result) == len(store):
              
          if len(each_word) < shortest_length:
            shortest_length = len(each_word)
                  
            output = each_word
      except:
        pass
                
    return output

#Add tests
def shortest_completing_word_test():

  input_licensePlate1 = "1s3 PSt"
  input_licensePlate2 = "1s3 456"
  input_licensePlate3 = "GrC8950"

  input_words1 = ["step","steps","stripe","stepple"]
  input_words2 = ["looks","pest","stew","show"]
  input_words3 = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
  

  expected_output1 = "steps"
  expected_output2 = "pest"
  expected_output3 = "according"

  return ( expected_output1 == shortest_completing_word(input_licensePlate1, input_words1), expected_output2 == shortest_completing_word(input_licensePlate2, input_words2), expected_output3 == shortest_completing_word(input_licensePlate3, input_words3) )

print(shortest_completing_word_test())

#Solution
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        store = {}
        shortest_length = 9999999999
        licensePlate = licensePlate.lower()
        licensePlate = list(licensePlate)
        output = ""

        for i in range(0, len(licensePlate)):

            try:
                int_converted = int(licensePlate[i])

            except:
                if licensePlate[i].strip() == '':
                    pass
                elif licensePlate[i] not in store:
                    store[licensePlate[i]] = 1
                else:
                    store[licensePlate[i]] = store[licensePlate[i]] + 1

        for each_word in words:

            interim_store = {}

            for i in range(0, len(each_word)):

                if each_word[i] not in interim_store:
                    interim_store[each_word[i]] = 1
                else:
                    interim_store[each_word[i]] = interim_store[each_word[i]] + 1

              #Compare
            try:
                result = {key: value for key, value in store.items() if store[key] <= interim_store[key]}

                if len(result) == len(store):

                    if len(each_word) < shortest_length:
                        shortest_length = len(each_word)

                        output = each_word
            except:
                pass

        return output





