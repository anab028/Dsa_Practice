def morethanbyk(arr,k):
  n=len(arr)
  x=n//k

  freq={}
  
  for num in arr:
    freq[num]=freq.get(num,0)+1

  sorted_keys=sorted(freq.keys())

  for key in sorted_keys:
    if freq[key]>x:
      print(key)


arr=[3, 4, 2, 2, 1, 2, 3, 3]
morethanbyk(arr,4)
