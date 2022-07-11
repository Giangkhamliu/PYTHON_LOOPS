# 1 2 3 
# 2 3 4 
# 3 4 5 
n=int(input("Enter no.of rows."))
i=1
while i<n+1:
    j=1
    while j<n+1:
        print(i+j-1,end=" ")
        j+=1
    print()
    i+=1