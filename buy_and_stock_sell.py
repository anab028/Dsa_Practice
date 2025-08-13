def buy_stock(arr):

    minsofar=arr[0]
    res=0

    for i in range(len(arr)):
      minsofar=min(minsofar,arr[i])

      res=max(res,arr[i]-minsofar)
    return res 
  
prices = [7, 10, 1, 3, 6, 9, 2]
print(buy_stock(prices))