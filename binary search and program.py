def binary_search(arr,first,last,num):
    if first>last:
        return -1
    mid==(first+last)/2
    if num==arr[mid]:
        return mid
    elif num>arr[mid]:
        return binary_search(arr,mid+1,last,num)
    else:
        return binary_search(arr,first,mid+1,num)
    arr = list(map(int,input("enter the elements: ")))
    