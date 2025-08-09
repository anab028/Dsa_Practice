def maxi_sub_array_sum(arr):
  max_ending=arr[0]
  res=arr[0]
  for i in range(len(arr)):
    max_ending=max(max_ending+arr[i],arr[i])  
    res=max(max_ending,res)

  return res 



arr = [2, 3, -8, 7, -1, 2, 3]
print(maxi_sub_array_sum(arr))