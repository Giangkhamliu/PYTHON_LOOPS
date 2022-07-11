n=int(input("Enter the number:"))
i=0
while i<n:
   k=ord("a")
   j=0
   while j<i:
      print(chr(int(k)),end=" ")
      k+=1
      j+=1
   print()
   i+=1


