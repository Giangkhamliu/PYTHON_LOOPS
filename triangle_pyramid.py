#TWO TRIANGLE
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 


# n=int(input("Enter any no. of rows:"))   
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#             print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

i=0
while i<5:
    j=i
    while j<5:
        print(" ",end=" ")
        j+=1
    j=0
    while j<i:
        print("*",end=" ")
        j+=1
    j=0
    while j<i+1:
        print("*",end=" ")
        j+=1
    print()
    i+=1
