n = int(input("Enter a number: "))

total = 0
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
        count += 1

print("Sum of even numbers:", total)
print("Number of even numbers:", count)