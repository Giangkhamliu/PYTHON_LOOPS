# 1+2+6+......+n

n=int(input("Enter the numbers:"))
i=1
series=1
sum=0
while i<=n:
    series*=i
    sum=sum+series
    i+=1
print(sum)