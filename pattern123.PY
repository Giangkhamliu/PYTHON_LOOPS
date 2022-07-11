# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

i=0
num=1
while i<5:
    j=0
    while j<i:
        print(num,end=" ")
        num+=1
        j+=1
    print()
    i+=1
