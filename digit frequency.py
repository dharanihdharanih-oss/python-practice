# 3b) Read a multi-digit number from the console. Develop a program 
# to print the frequency of each digit with suitable message.

num = input("Enter the number: ")
print("The Entered number is:", num)

uniq_dig = set(num)
print("Unique Digit:", uniq_dig)

for element in uniq_dig:
    print(element, "occurs", num.count(element), "times")