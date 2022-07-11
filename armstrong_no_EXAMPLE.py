n=int(input("Enter the number:"))
sum=0
n1=n
while n1>0:
    digit=n1%10
    sum+=digit**3
    n1=n1//10
if n==sum:
    print(n,"armstrong")
else:
 print("Armstrong")


