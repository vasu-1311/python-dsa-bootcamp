def selection_sort(num):
    n=len(num)
    for i in range (0,n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
             min_index=j
        num[i],num[min_index]=num[min_index],num[i]


arr=[65,94,12,10,1]
selection_sort(arr)
print(arr)