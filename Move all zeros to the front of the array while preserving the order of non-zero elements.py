def move4(arr):

  right=len(arr)-1

  for left in range(len(arr)-1,-1,-1):
    if arr[left]!=0:
      arr[right]=arr[left]
      right -=1

  for i in range(right,-1,-1):
    arr[i]=0

  


arr=[1,2,3,10,0,4,0,5]
move4(arr)
arr