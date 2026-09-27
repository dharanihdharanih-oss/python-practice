# 2a) Develop a python program to generate n fibonacci numbers

n = int(input("Enter value for n: "))
first_number = 0
second_number = 1

print("Fibonacci Series")
print(first_number)
print(second_number)

for i in range(2, n):
    next_number = first_number + second_number
    print(next_number)
    first_number = second_number
    second_number = next_number