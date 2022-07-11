# n=int(input("Enter the number:-"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print(j+1,end=" ")
#     print()


    
i=0
while i<5:
    j=0
    while j<i+1:
        print(" ",end=" ")
        j+=1
    while j<5:
        print(j,end=" ")
        j+=1
    i+=1
    print()

