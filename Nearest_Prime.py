def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return True
    else:
        return False
        
def previous_prime(n):
    while is_prime(n)==False:
        n=n-1
    return n
def next_prime(n):
    while is_prime(n)==False:
        n=n+1
    return n
def nearest_prime(n):
    a=previous_prime(n)
    b=next_prime(n)
    if n-a<=b-n:
        print(a)
    else:
        print(b)
s=int(input())
for i in range(s):
    x=int(input())
    nearest_prime(x)