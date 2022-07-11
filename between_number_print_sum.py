num1=int(input("Enter the number:-"))
num2=int(input("Enter the second number:-"))
sum=0
while num1<=num2:
    if num1%3==0:
        sum+=num1
    num1+=1
print(sum)

