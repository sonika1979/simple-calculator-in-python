a= input("enter a\n")
x = int (a)
print("a=",x)
b = input("enter b\n")
y = int(b)
print("b=",y)
print("enter which operation from 0-4 which has to be performed:")
i = input()
j = int(i)
if j==0:
    r=x+y
    print("sum=",r)
elif j==1:
    r=x-y
    print("difference=",r)
elif j==2:
    r=x*y
    print("product=",r)
elif j==3:
    r=x//y
    p=x%y
    print("quotient=",r)
    print("remainder=",p)
elif j==4:
    r=x**y
    print("a raised to b=",r)
else:
    print("wrong selection. check ur options")

print("CALCULATOR IS HAPPY :-D")
