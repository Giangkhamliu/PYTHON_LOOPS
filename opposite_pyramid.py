#  * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

n=int(input("Enter any no. of rows:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()



