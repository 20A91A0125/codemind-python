def add_digits(n):
    sum=0
    while (n>0):
        r=n%10
        sum+=r
        n=n//10
    return sum

a=int(input())
while(a>9):
    a=add_digits(a)
print(a)