def next_permutation(s:str):
  arr=list(s)
  n=len(arr)
  i=n-2
  j=n-1

  while i>=0 and arr[i]>=arr[i+1]:
    i-=1
  
  if i<0 :
    return -1

  while arr[j] <=arr[i]:
    j-=1

  arr[i],arr[j]=arr[j],arr[i]
  arr[i+1:]=reversed(arr[i+1:])
  return "".join(arr)
  
print(next_permutation("abdc"))
print(next_permutation("hefg"))
print(next_permutation("bb"))
print(next_permutation("dcba"))
print(next_permutation("abbb"))
