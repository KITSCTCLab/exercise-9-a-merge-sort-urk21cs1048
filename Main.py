def merge_sort(data) -> None:
  if len(data) >1:
    mid = (len(data))//2
    data_left = data[:mid]
    data_right = data[mid:]
    merge_sort(data_left)
    merge_sort(data_right)
 
    i = 0
    j = 0
    k = 0

    while i<len(data_left) and j<len(data_right):
      if data_left[i] <= data_right[j]:
        data[k] = data_left[i]
        i+=1
      else:
        data[k] = data_right[j]
        j+=1
      k+=1

    while i < len(data_left):
      data[k] = data_left[i]
      i+=1
      k+=1
    while j < len(data_right):
      data[k] = data_right[j]
      j+=1
      k+=1
    return data
 


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
