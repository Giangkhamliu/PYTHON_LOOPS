n=int(input("Enter the number:"))
i=0
while i<n:
   k=ord("A")+i
   j=0
   while j<i+1:
      print(chr(int(k)),end=" ")
      k-=1
      j+=1
   print()
   i+=1

