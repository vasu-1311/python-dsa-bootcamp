def find_second_largest(arr):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(arr)
    for i in range(0,n):
        largest=max(largest,arr[i])
    for i in range(0,n):
        if arr[i]>s_largest and arr[i]!=largest:
            s_largest=arr[i]
    return s_largest
arr=[55,67,54,12,89,90,54,78]   
print(find_second_largest(arr))