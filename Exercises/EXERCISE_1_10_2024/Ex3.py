numbers = input("Enter a number: ").split()
print(numbers)
average = 0
for _ in numbers:
    average += int(_)
print(average/len(numbers))