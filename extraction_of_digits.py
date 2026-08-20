#count number
n=12345
num=n
count=0
while num>0:
    count+=1
    num=num//10
print(count)

#check Palindrome
n=121
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
print( n==result)

#armstrong number
n=153
num=n
total=0
nod=len(str(num))
while num>0:
    
    ld=num%10
    total+=ld**nod
    num=num//10
print(total==n)

