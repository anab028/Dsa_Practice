

def partition(arr,l,r):
  pivot=arr[r]
  i=l
  for j in range(l,r):
    if arr[j]<=pivot:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
  arr[i],arr[r]=arr[r],arr[i]
  return i


def quick_Select(arr,l,r,k):

  pos=partition(arr,l,r)

  if pos-l==k-1:
    return arr[pos]
  elif pos-l>k-1:
    return quick_Select(arr,l,pos-1,k)
  else:
    return quick_Select(arr,pos+1,r,k-(pos-l+1))

arr=[12,3,5,7,4,19,26]
s=quick_Select(arr,0,len(arr)-1,3)
s

