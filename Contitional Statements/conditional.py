# Simple if statement
# if condition:
    # instructions

# age = 10
# if age >= 18:
#     print("You are an adult")

# num = input("Enter a number: ")
# num = int(num)
# if num % 2 == 0:
#     print("The number is even")

# if-else Statement
# if condition:
    # instructions
# else:
    # instructions

# num = input("Enter a number: ")
# num = int(num)
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# elif Statement
# if condtion:
#     # instructions
# elif condition:
#     # instructions
# elif condition:
#     # instructions
# else:
#     # instructions


# if 10> 10:
#     print("10 is greater than 10")
# if 10 < 10:
#     print("10 is less than 10")
# if 10 == 10:
#     print("10 is equal to 10")

age = input("Enter your age: ")
age = int(age) # 19
if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are an adult")
elif age >= 65 and age <= 100:
    print("You are a senior citizen")
else:
    print("Invalid age")