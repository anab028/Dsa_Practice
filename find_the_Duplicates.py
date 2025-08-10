def duplicates(arr):

  map={}
  duplicates=[]

  for i in arr:
    if i not in map:
      map[i]=1
    else:
      map[i]+=1
  for i in map:
    if map[i]>1:
      duplicates.append(i)
  return duplicates




arr= [1, 2, 3, 6, 3, 6, 1]

ans=duplicates(arr)
ans