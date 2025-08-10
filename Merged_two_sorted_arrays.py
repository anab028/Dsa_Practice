def merged(arr1,arr2):

  n=len(arr1)
  m=len(arr2)

  merged=[]

  i,j,k=0,0,0

  while i<n and j<m:
    if arr1[i]<arr2[j]:

      merged.append(arr1[i])
      i+=1

    else: 
      merged.append(arr2[j])
      j+=1
  
   

  while i<n:
    merged.append(arr1[i])
    i+=1
    k+=1

  while j<m:
    merged.append(arr2[j])
    j+=1
    k+=1

  return merged


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

ans=merged(arr1,arr2)
ans