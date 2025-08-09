arr=[1,0,2,0,2,0,1,2,0]
new_arr=[]
count_zero=0
count_one=0
count_two=0

for i in range(len(arr)):
  if arr[i]==0:
    count_zero +=1
  elif arr[i]==1:
    count_one +=1
  elif arr[i]==2:
    count_two +=1

for i in range(count_zero):
  new_arr.append(0)
for i in range(count_one):
  new_arr.append(1)
for i in range(count_two):
  new_arr.append(2)

new_arr




  