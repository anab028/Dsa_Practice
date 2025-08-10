def minimize_the_maximum_diff(arr,k):

  n=len(arr)

  arr.sort()

  res=arr[n-1]-arr[0]

  for i in range(1,n):

    if arr[i]-k<0 :
      continue

    minH=min(arr[0]+k,arr[i]-k)
    maxH=max(arr[n-1]-k,arr[i-1]+k)
    res=min(res,maxH-minH)

  return res

k = 6
arr = [12, 6, 4, 15, 17, 10]
print(minimize_the_maximum_diff(arr,k))



  