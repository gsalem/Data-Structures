'''
Binary Search using recursion

'''
def binary_search(arr,value):
  if len(arr)==0 or (len(arr)==1 and arr[0]!=value):
    return print("%d not found" % value)

  mid = arr[len(arr)//2]

  if value == mid:
    return print("%d found" % value)
  if value < mid:
    return binary_search(arr[:len(arr)//2],value)
  if value > mid:
    return binary_search(arr[len(arr)//2+1:],value)

arr=[0,2,6,6,9,13,17,27,35]
binary_search(arr,0)
binary_search(arr,27)
binary_search(arr,6)
binary_search(arr,999)
binary_search(arr,1)
binary_search(arr,-1)