print ("THIS = BINARY SEARCH")
def binarysearchpro(arr,start,end,x):
  if end >= start:
    mid = start + (end - start)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
     return binarysearchpro(arr,start,mid-1,x)
    else:
     return binarysearchpro(arr,start,mid-1,x)
  else:
     return-1
  arr = sorted (['a','q','w','e','r','t','y','u','i','o','p'])
  x = input ("enter the number of your choice")
  result = binarysearchpro (arr,0,len(arr)-1,x)
  if result != -1:
    print ("the number is present at the index"+str(result)
  else :
    print("element is not in the array")