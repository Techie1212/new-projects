l1=[]
number=int(input("enter any number:"))
for i in range(1,number+1):
    i=int(input("enter a value:"))
    l1.append(i)
for n in l1:
    if(n%2!=0):
         n=n+1
    l1.append(n)
for m in l1:
      if(m%2==0):
         m=m+2
      l1.append(m)
print(l1)
