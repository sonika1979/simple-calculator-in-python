int a= input("enter a\n")

print("a=",a)
int b = input("enter b\n")

print("b=",b)
print("enter which operation from 0-4 which has to be performed:/n 1.add/n2.sub/n3.mult/n4.div/n")
int option = input()

if option==0:
    r=a+b
    print("sum=",r)
elif option==1:
    r=a-b
    print("difference=",r)
elif option==2:
    r=a*b
    print("product=",r)
elif option==3:
    r=a//b
    p=a%b
    print("quotient=",r)
    print("remainder=",p)
elif option==4:
    r=a**b
    print("a raised to b=",r)
else:
    print("wrong selection. check ur options")

print("CALCULATOR IS HAPPY :-D")
