###Name pattern
name=input("Enter any name:")
length=len(name)
for i in range(length):
    for j in range(i+1):
        print(name[j],end=" ")
    print()




