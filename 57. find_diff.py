
def find_difference(s, t):

  store_1 = list(s)
  store_2 = list(t)

  master_store = {}


  for i in range(0, len(store_1)):

    if store_1[i] not in master_store:
      master_store[store_1[i]] = 1

    else:
      master_store[store_1[i]] = master_store[store_1[i]] + 1

  for i in range(0, len(store_2)):

      if store_2[i] not in master_store:
        return store_2[i]

      else:
        master_store[store_2[i]] = master_store[store_2[i]] - 1

        if master_store[store_2[i]] == 0:

          del master_store[store_2[i]]
              
  return master_store.keys()[0]
