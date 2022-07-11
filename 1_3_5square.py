n=int(input("Enter the numbers:"))
num=1
i=1
while i<=n:
    j=1
    while j<=n:
        print(num,end=" ")
        num+=2
        j+=1
    print()
    i+=1
