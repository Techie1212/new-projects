#print prime numbers in a given range.
number=int(input("enter any number:"))*2
for i in range(1,number+1):
   count=0
   for j in range(1,i+1):
       if(i%j==0):
           count=count+1
   if(count==2):
       print(i)
#print armstrong number.
while(True):
    value=input("enter any string:")
    if(value=="exit"):
       print("Bye!!")
       break
    number=int(value)
    count=0
    number1=number
    while(number!=0):
         rem=number%10
         number=number//10
         count=count+1
    sum=0
    k=number1
    while(number1!=0):
        rem=number1%10
        number1=number1//10
        sum=sum+rem**count
    if(sum==k):
        print("it is an amrstrong")
    else:
        print("not")
   
