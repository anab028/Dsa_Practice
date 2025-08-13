def commonElements(arr1,arr2,arr3):

  count={}

  for ele in arr1:
    count[ele]=1
  for ele in arr2:
    if count.get(ele)==1:
      count[ele]=2
  for ele in arr3:
    if count.get(ele)==2:
      count[ele]=3
  
  result=[]

  for ele in count:
    if count[ele]==3:
      result.append(ele)
  return result


arr1 = [1, 5, 10, 20, 30]
arr2 = [5, 13, 15, 20]
arr3 = [5, 20]


common = commonElements(arr1, arr2, arr3)
if len(common) == 0:
    print(-1)
common
