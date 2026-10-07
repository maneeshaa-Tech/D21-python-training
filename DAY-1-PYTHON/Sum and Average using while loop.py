n = int(input("Enter N: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

average = sum / n

print("Sum =", sum)
print("Average =", average)