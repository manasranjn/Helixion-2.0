# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# # print("Division: ",a/b)

# try:
#     print("Division: ",a/b)
# except:
#     print("You cannot divide by zero")
# finally:
#     print("Always executes")

try:
    a = int("Hello")
except Exception:
    print("Something went wrong")
except ValueError:
    print("Invalid input")
except TypeError:
    print("Invalid type")