def reconstruct_trip(tickets):
  ht = {}
  reconstruct_list = []
  for ticket in tickets:
    ht[ticket[0]] = ticket[1]
  
  reconstruct_list.append(ht[None])
  print("None", reconstruct_list)

  for i in range(1, len(ht)-1):
    try:
      reconstruct_list.append(ht[reconstruct_list[i-1]])
    except:
      reconstruct_list = []
      print(reconstruct_list)
      return reconstruct_list
  print(reconstruct_list)
  return reconstruct_list

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
