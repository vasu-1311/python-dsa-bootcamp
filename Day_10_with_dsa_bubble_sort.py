def bubble_sort(num):
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
              num[j],num[j+1]=num[j+1],num[j]
arr=[4,6,1,8,5,6,1]
bubble_sort(arr)
print(arr)