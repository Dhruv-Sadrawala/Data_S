marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
avg = sum(marks) / 3
print(f"Average Marks: {avg}")