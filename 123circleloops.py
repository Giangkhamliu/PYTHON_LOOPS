row=3
col=3
for i in range(row):
     for j in range(col):
        if j==0:print(i+1,end=" ")   
print()
for i in range(row):
     for j in range(col):
       if i==1 and j==0:print("8",end=" ")
       if i==1 and j==1:print("9",end=" ")
       if i==1 and j==2:print("4")
for i in range(row):
    for j in range(col):
      if i==2: print(7-j,end=" ")

print()



for i in range(3):
     for j in range(3):
        if j==0:print(i+1,end=" ")   
print()
for i in range(3):
     for j in range(3):
       if i==1 and j==0:print(9-i,end=" ")
       if i==1 and j==1:print(10-i,end=" ")
       if i==1 and j==2:print(3+i)
for i in range(3):
    for j in range(3):
      if i==2: print(7-j,end=" ")
      