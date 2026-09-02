num=[45,32,78,99,12,33]
n=len(num)
largest=num[0]
for i in range(0,n):
    largest=max(largest,num[i])
print(largest)


#method two
num=[45,32,78,99,12,33]
n=len(num)
largest=num[0]
for i in range(0,n):
    if largest<num[i]:
        largest=num[i]
print(largest)