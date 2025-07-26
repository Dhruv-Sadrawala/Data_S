#Create menu-driven calculator program using a module. (add, subtract, multiply,divide)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def add(n1,n2):
	su= n1+n2
	print("Sum is :",su)

def deff(n1,n2):
	deff= n1-n2
	print("Difference is :",deff)

def pro(n1,n2):
	pro= n1*n2
	print("Product is :",pro)

def div(n1,n2):
	rem= n1/n2
	print("Quotient is :",rem)


ch = int(input("Enter choice: "))

while (ch != 5):
	print("1 for Sum")
	print("2 for Difference")
	print("3 for Product")
	print("4 for Quotient")
	print("5 for Exit")

	if ch == 1:
		add(n1,n2)
	elif ch == 2:
		deff(n1,n2)
	elif ch == 3:
		pro(n1,n2)
	elif ch == 4:
		div(n1,n2)
	else:
		print("Invalid Choice")

	ch = int(input("Enter choice: "))