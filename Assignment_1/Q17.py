marks = [int(x) for x in input("Enter marks separated by space: ").split()]
print("Average:", sum(marks)/len(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))