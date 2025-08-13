def sub_array_with_zero_sum(arr):

  s=set()
  s_sum=0
  for i in range(len(arr)):
    s_sum +=arr[i]
    if s_sum ==0 or s_sum in s:
      return True
    s.add(s_sum)
  return False


arr = [-3, 2, 3, 1, 6]
print(sub_array_with_zero_sum(arr) ) 