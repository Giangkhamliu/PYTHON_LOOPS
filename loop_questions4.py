# Write a program to display all even numbers that fall between two numbers (exclusive both numbers)
# entered by the user
lower=int(input("Enter any number"))
upper=int(input("Enter any number:"))
i=1
while i<upper: 
    if i%2==0:
        print(i)
    i+=1

