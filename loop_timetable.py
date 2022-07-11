#  Write a program to print a table of a number entered from the user.
n=int(input("Enter any number:"))
i=1
while i<=10:
    if i!=0:
        print(n,"*",i,"=",n*i)
    i+=1

