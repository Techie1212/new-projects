value=input("enter any number:")
while(True):
    if(value=="quit"):
       print("bye!!")
       break
    number=int(value)
    k=number
    sum=0
    while(number!=0):
       rem=number%10
       number=number//10
       sum=sum*10+rem
    if(sum==k):
       print("it is palindrome")
    else:
       print("not")
