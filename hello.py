num1=float('-inf')
num2=float('inf')

def max_el(arr):
    max=num1
    for i in arr:

        if i>max:
            max=i
    return max
def min_el(arr):
    min=num2
    for i in arr:
        if i<min:
            min=i
    return min
          
arr=[1,2,30,4,5,6,7,8]
max=max_el(arr)
min=min_el(arr)
print(max)
print(min)