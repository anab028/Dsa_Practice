def longest_consucutive_array(arr):

  st=set(arr)
  cur=res=cnt=0

  for val in arr:
    st.add(val)

  for val in st:
    if val-1 not in st:
      cur=val
      cnt=0
      while cur in st:
        cur+=1
        cnt+=1
      res=max(res,cnt)
  return res


  

arr = [2, 6, 1, 9, 4, 5, 3]

print(longest_consucutive_array(arr))
