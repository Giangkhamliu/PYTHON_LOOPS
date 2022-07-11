n=int(input("Enter the number:"))
i=0
while i<n:
  k=ord("E")-i
  print(chr(int(k)),end=" ")
  j=n-1
  while j>i:
      print(chr(int(k)),end=" ")
      
      j-=1
  print()
  i+=1



