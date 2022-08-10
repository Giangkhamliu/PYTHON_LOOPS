n=int(input("enter the number:"))
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
k=sum
while k>0:
    m=k%10
    v=m**2
    k=k//10
    print(v,end="")