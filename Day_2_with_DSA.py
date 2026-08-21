#print all the factors of given number
n=20
num=n
result=[]
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print(result)
#better result
n=20
num=n
result=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)
#introduction to hasshing in python
n=[1,2,3,2,4,3,2,1]
m=[4,3,2,1,3,6,8,1]
for i in m:
    count=0
    for num in n:
        if num==i:
            count+=1
    print(count)