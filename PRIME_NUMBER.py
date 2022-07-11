num=int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime no.")
        break
    else:
            print(num,"a prime no.")
else:
        print(num,"not prime")
