#Find the second largest number from a list .
n = int(input("Enter number of elements: "))
lis1 = []
for i in range(n):
    e = int(input("Enter element: "))
    lis1.append(e)

print("List:",lis1)

lis1.sort()
if len(lis1)<2:
    print("Less Elements.")
else:
    print("Second Largest element: ",lis1[-2])