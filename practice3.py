l1=[]
l2=[]
number=int(input("enter any number:"))
for i in range(1,number+1):
    i=int(input("enter any number:"))
    l1.append(i)
    i=input("enter any value:")
    l1.append(i)
l1.insert(1,"prabha")
l2=l1.copy()
print("l2 is = ",l2)

