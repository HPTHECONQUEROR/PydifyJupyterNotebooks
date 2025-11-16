
def add(*args):
    print("Raw args",args)
    args = args[0]
    total = 0
    for i in args:
        total += i
    return total

while True:
	cal = int(input("Enter the choice \n1.Add\n8.Exit\n"))
	if cal == 8:
		break
	mul_inputs = input()
	mul_inputs = mul_inputs.split(",")
	integers_list = []
	for i in mul_inputs:
		integers_list.append(int(i))
	
	if cal == 1:
		print(add(integers_list))
	
