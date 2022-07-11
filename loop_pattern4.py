#  1 1 1 1 1
#  2 2 2 2 
#  3 3 3 
#  4 4 
#  5 
i=0
while i<5:
    j=i
    while j<5:
        print(i+1,end=" ")
        j+=1
    print()
    i+=1

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
i=1
while i<=5:
    j=5
    while j>=i:
        print(i,end=" ")
        j-=1
    print()
    i+=1

