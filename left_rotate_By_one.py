def rotate(arr):
  temp=arr[-1]
  for i in range(len(arr)-1,-1,-1):
    arr[i]=arr[i-1]
  
  arr[0]=temp


arr=[1,2,3,4,5,6]

rotate(arr)
arr