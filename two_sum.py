def two_sum(arr,target):

  freq={}
  count=0
  pairs=[]

  for nums in arr:
    complement=target-nums
    if complement in freq:
      count +=freq[complement]
      for i in range(freq[complement]):
        pairs.append((nums,complement))
    freq[nums]=freq.get(nums,0)+1

  return pairs
    



arr=[1,5,7,-1,5]
target=6
arr=two_sum(arr,target)
arr