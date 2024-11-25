def Add(x,y):
    return x+y
def Sub(x,y):
    return x-y
def Mul(x,y):
    return x*y
def Div(x,y):
    if y!=0:
        return x/y
    else:
        print('Division Not Possible!!')

x=int(input("Enter x: "))
y=int(input("Enter y: "))
op=input("Enter operator to perform OPERATION(+,-,*,/) : ")
if op=='+':
    result=Add(x,y)
elif op=='-':
    result=Sub(x,y)
elif op=='*':
    result=Mul(x,y)
elif op=='/':
    result=Div(x,y)
else:
    print("You have entered an Invalid operator!!")
print("Result is :",result)