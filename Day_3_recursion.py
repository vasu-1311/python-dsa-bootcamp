#head recursion
count=0
def fun():
    global count
    if count==4:
        return
    count+=1
    fun()
    print('vasu')
fun()
#1
def print_count(n):
    if n==0:
        return
    print_count(n-1)
    print(n)
print_count(5)

