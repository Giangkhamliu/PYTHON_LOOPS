user=int(input("Enter the number:"))
for num in range(1,user+1):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print(num)