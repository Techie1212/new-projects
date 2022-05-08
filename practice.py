while(1):
  str=input("enter any input:")
  if(str=="quit"):
    print("bye!!")
    break
  if(str[::-1]==str):
    print("it is palindrome")
  else:
    print("not")
    
