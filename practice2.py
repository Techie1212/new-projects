class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("ajay",21)
print(p1.name)
print(p1.age)
del p1
#
class Myclass:
    x=5
p1=Myclass()
print(p1.x)
#
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1=person("Ajay",21)
p1.myfunc()
print(p1.name)
print(p1.age)
#
class maths:
    def __init__(self,number):
        self.number=number
    def prime(number):
        count=0
        for i in range(1,number+1):
            if(i%2==0):
              count=count+1
        if(count==2):
            print("it is prime")
        else:
            print("it is not")
number=int(input("enter any number:"))
p1=prime(number)
print(p1)
         
