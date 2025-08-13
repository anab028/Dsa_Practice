def rearrange(arr):
  pos=[]
  neg=[]

  for i in arr:
    if i<0:
      pos.append(i)
    else:
      neg.append(i)

  posidx=0
  negidx=0
  i=0

  while posidx <len(pos) and negidx<len(neg):
    if i%2==0:
      arr[i]=pos[posidx]
      posidx+=1
      i+=1
    else:
      arr[i]=neg[negidx]
      negidx+=1
      i+=1

  while posidx<len(pos):
    arr[i]=pos[posidx]
    posidx+=1
    i+=1

  while negidx<len(neg):
    arr[i]=neg[negidx]
    negidx+=1
    i+=1
   

arr = [1, -2, 3, -4, -1, 4]
rearrange(arr)
arr
