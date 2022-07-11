user=int(input("Enter any 2 number:"))
store=user
n=str(len(str(user)))
i=1
while i<int(n):
    user=user//10
    digit=user*user
    num=store%10
    digit_1=num*num
    i+=1
print(str(digit)+str(digit_1))

#3numbers
user=int(input("Enter any 3 number:"))
store=user
i=1
while i<3:
    user=user%10
    result=user*user
    num=store//10
    user_1=num%10
    result_1=user_1*user_1
    digit=num//10
    result_2=digit*digit
    i+=1
print(str(result_2)+str(result_1)+str(result))

