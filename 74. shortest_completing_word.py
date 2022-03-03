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
