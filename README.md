This repository contains a video presentation and Python implementation of the Binary Search algorithm.
<br>
📌 What is Binary Search?<br>

Binary Search is an efficient searching algorithm used to find an element in a sorted list.
It works by repeatedly dividing the search interval in half.<br>

Time Complexity: O(log n)<br>
Works only on sorted data<br>


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
    
