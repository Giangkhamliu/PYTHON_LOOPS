n=int(input("enter the number:"))
fact=1
while n>0:
    fact=fact*n
    n-=1
print(fact)

#FOR LOOP

n=int(input("Enter the number:"))
result=1
for i in range(n,0,-1):
    result*=i
print("factorial of ",n,"is",result)