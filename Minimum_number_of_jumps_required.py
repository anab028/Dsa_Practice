def jump(arr):

 maxreach=curr=jumping=0

 for i in range(len(arr)):
   maxreach=max(maxreach,arr[i]+i)

   if maxreach > len(arr)-1:
    return jumping+1

   if i==curr:


    if i==maxreach:
      return -1

    else:
      curr=maxreach
      jumping +=1

 return jumping 


    


arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

ans=jump(arr)
ans

