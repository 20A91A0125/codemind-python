def s(n):
    t=n
    while n>0:
        r=n%10
        if r==0 or t%r!=0:
            return False
        n=n//10
    return True
i=int(input())
j=int(input())
for a in range(i,j+1):
    if s(a)==True:
        print(a,end=' ')