n = int(input("Enter a number: "))
rev = 0

while n > 0:
	rev = rev + n%10 
	rev = rev * 10 
	n =   n//10

print(rev//10)
