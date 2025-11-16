def add(*args):
    total=0
    for i in args:
        total+=i
    return total

i=0
while True:
    cal=int(input("choose operation \n1.Add\n2.Sub\n3.mul\n4.div\n5.Floor div\n6.Exponential\n7.Modulus\n8.Exit\n"))
    if cal ==8:
        break

    a=int(input("enter numbers u want to calculate: "))

    if cal == 1:
        print(add(a))
    elif cal == 2:
        print("subtraction of ",a,"and",b,"is",sub(a))

    elif cal == 3:
        print("Multiplication of ",a,"and",b,"is",mul(a))

    elif cal == 4:
        print("Division of ",a,"and",b,"is",div(a,b))

    elif cal == 5:
        print("Integer Division of ",a,"and",b,"is",floor_div(a,b))

    elif cal == 6:
        print("Exponential of ",a,"and",b,"is",exp(a,b))

    elif cal == 7:
        print("Modulus of ",a,"and",b,"is",mod(a,b))





