def recursive_fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return recursive_fibo(n-1)+recursive_fibo(n-2)

def iter_fibo(n):
    a,b=0,1
    if n==1:
        return a
    elif n==2:
        return 1
    while n-2>0:
        c=a+b
        a,b=b,c
        n=n-1
    return c


imp=int(input("Enter number of fibonacci numbers required: "))


iter,rec=[],[]
for i in range(1,imp+1):
    rec.append(str(recursive_fibo(i)))
    iter.append(str(iter_fibo(i)))
print("Recursive sequence is "+ " ".join(rec))
print("Iterative sequence is "+ " ".join(iter))
    