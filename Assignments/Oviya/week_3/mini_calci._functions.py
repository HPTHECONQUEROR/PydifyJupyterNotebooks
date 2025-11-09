def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def floor_div(a, b):
    return a // b
def exp(a, b):
    return a ** b
def mod(a, b):
    return a % b


cal=int(input("choose operation \n1.Add\n2.Sub\n3.mul\n4.div\n5.Floor div\n6.Exponential\n7.Modulus\n8.Exit\n"))

a=int(input("Enter first no: "))
b=int(input("Enter second no: "))

if cal == 1:
    print("Addition of ",a,"and",b,"is",add(a,b))
elif cal == 2:
    print("subtraction of ",a,"and",b,"is",sub(a,b))

elif cal == 3:
    print("Multiplication of ",a,"and",b,"is",mul(a,b))

elif cal == 4:
    print("Division of ",a,"and",b,"is",div(a,b))

elif cal == 5:
    print("Integer Division of ",a,"and",b,"is",floor_div(a,b))

elif cal == 6:
    print("Exponential of ",a,"and",b,"is",exp(a,b))

elif cal == 7:
    print("Modulus of ",a,"and",b,"is",mod(a,b))



