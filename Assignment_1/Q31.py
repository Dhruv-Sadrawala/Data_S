nums = [int(x) for x in input("Enter numbers: ").split()]
even_nums = [n for n in nums if n % 2 == 0]
print("Even numbers:", even_nums)