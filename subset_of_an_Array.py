def is_subset(arr1,arr2):

  i,j=0,0

  arr1.sort()
  arr2.sort()

  while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
      i+=1
    elif arr1[i]==arr2[j]:
      i+=1
      j+=1
    else:
      return False
  return j==len(arr2)


a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

if is_subset(a,b):
  print("True")
else:
  print("False")