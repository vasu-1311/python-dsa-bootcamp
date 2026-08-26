def reverse_array(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_array(arr,left+1,right-1)
mylist=[1,2,3,4,5,6,7]
reverse_array(mylist,0,len(mylist)-1)
print(mylist)