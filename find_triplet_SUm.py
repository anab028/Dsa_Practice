def hasTripletSum(arr, target):
    

    n=len(arr)

    a=b=c=0

  

    for i in range(n-2):
      st=set()

      for j in range(i+1,n):
        value =target-arr[i]-arr[j]
        
        

        if value in st:

         

          return True
        st.add(arr[j])

    return False






arr = [1, 4, 45, 6, 10, 8]
target = 13
if hasTripletSum(arr, target):
        print("true")
else:
        print("false")