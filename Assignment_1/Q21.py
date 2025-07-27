nums = [int(x) for x in input("Enter numbers: ").split()]
nums.sort()
print("Second largest number:", nums[-2])