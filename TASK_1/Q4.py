#Remove duplicates items from list without using set

n = int(input("Enter number of elements: "))
lis1 = []
for i in range(n):
    e = int(input("Enter element: "))
    lis1.append(e)

print("List:",lis1)

lis1 = list(dict.fromkeys(lis1))
print("Unique element list: ",lis1)