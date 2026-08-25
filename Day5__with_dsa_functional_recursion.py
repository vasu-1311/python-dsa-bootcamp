#parameterized function
# lets print sum of 1 to n using parameter
def fun(sum,i,n):
    if i>n:
        print(sum)
        return
    fun(sum+i,i+1,n)
fun(0,3,9)
#functional recursion
def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
print(fun(7))
