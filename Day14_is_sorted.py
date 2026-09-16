def is_sortd(num):
    n=len(num)
    for i  in range(0,n-1):
        if num[i]>num[i+1]:
            return False
    return True
num=[2,4,6,7,8,9,12]
print(is_sortd(num))