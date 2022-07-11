#1. Write a program to print the following using while loop
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

i=1
print("The First 10 Even numbers are:")
while i<=20:
    if i%2==0:
        print(i)
    i=i+1
print("The First 10 Odd Numbers are:")
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1
print("The First 10 Natural numbers are:")
i=1
while i<=10:
    if i!=0:
        print(i)
    i+=1
print("The First 10 Whole Number are:")
i=0
while i<10:
    print(i)
    i+=1

