def findMinDiff(arr,m):

  arr.sort()

  n=len(arr)

  res=float('inf')

  for i in range(n-m+1):

    diff=arr[i+m-1]-arr[i]

    res=min(res,diff)
  
  return res




arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(findMinDiff(arr, m))