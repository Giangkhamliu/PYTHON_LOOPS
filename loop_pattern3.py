#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 
i=0
while i<5:
    j=i+1
    while j<5:
        print("*",end=" ")
        j+=1
    while j<=5+i:
        print (i+1, end=" ")
        j+=1
    print()
    i+=1


