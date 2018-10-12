def get_indices_of_item_weights(weights, limit):
  ht = {}
  
  if len(weights) <= 1:
    return ()

  if len(weights) == 2:
    if (weights[0] + weights[1] == limit):
      return (1,0)
  
  for i, weight in enumerate(weights, 0):
    ht[weight] = i

  for key in ht:
    try:
      key_check = ht[limit-key]
      if(key_check):
        return (ht[limit-key], ht[key])
    except KeyError:
      pass

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 